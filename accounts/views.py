from django.contrib.auth.models import User
from django.core.mail import send_mail
from hostel.models import Room
from user.models import Profile
from django.shortcuts import *
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth import login as log, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db import IntegrityError


# Create your views here.

def login(request):
    context = {'form': UserAuthenticationForm()}
    if request.method == 'POST':
        uname = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(username=uname, password=passwd)
        if user is not None:
            if user.is_superuser or user.is_staff:
                log(request, user=user)
                return redirect('admin_page')
            else:
                log(request, user=user)
                return redirect('userhome')
        else:
            messages.add_message(request, level=messages.INFO, message="WRONG USERNAME OR PASSWORD")
            return render(request, 'accounts/login_page.html', context=context)
    else:
        return render(request, 'accounts/login_page.html', context=context)


def register(request):
    context = {'form': RegistrationForm()}
    if request.method == 'POST':
        fname = request.POST['FirstName']
        lname = request.POST['LastName']
        mail_id = request.POST['email']
        passwd1 = request.POST['password1']
        passwd2 = request.POST['password2']

        try:
            if User.objects.get(username=mail_id):
                messages.add_message(request, level=messages.WARNING, message="THIS EMAIL ID ALREADY REGISTERED")
                return redirect('signup_page')

        except (Exception, IntegrityError):
            if passwd1 != passwd2:
                messages.add_message(request, level=messages.INFO, message="PASSWORD NOT MATCHED")
                return redirect('signup_page')
            else:
                user = User.objects.create_user(username=mail_id, email=mail_id, password=passwd1, first_name=fname,
                                                last_name=lname)
                user.save()
                messages.add_message(request, level=messages.INFO, message="Username is your Email ID")
                log(request, user=user)
                # send mail after registration
                """
                send_mail(
                    'Registration Successful',
                    'Welcome to HMS. Thanks to using our service.',
                    'hms@management.com',
                    [request.user.email],
                )
                """
                return redirect('userhome')
    else:
        return render(request, 'accounts/register_page.html', context=context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('homepage')


@login_required
def adminlogin(request):
    cap = 0
    for obj in Room.objects.all():
        cap += obj.capacity

    users = (User.objects.count()) - (User.objects.filter(is_superuser=True).count())
    rooms = Room.objects.count()
    req = (Profile.objects.filter(apply=True).count()) - (Profile.objects.filter(payment_request=True).count())
    args = {'users': users, 'room': rooms, 'hostel': cap, 'req': req, 'current_user': request.user}
    return render(request, 'admin/adminpage.html', args)
