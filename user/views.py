from django.db.models import F
from django.dispatch import Signal
from django.shortcuts import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from datetime import date, timedelta

increment_signal = Signal(providing_args=['username'])


def increment_signal_receiver(sender, **kwargs):
    Room.objects.filter(room_id=Profile.objects.get(user__username=kwargs['username']).room.room_id).update(
        capacity=F('capacity') + 1)


@login_required
def profile(request):
    user = User.objects.get(username=request.user.username)
    data = Profile.objects.get(user=user)
    args = {'user': user, 'profile': data}
    return render(request, 'user/ProfileView.html', args)


@login_required
def update_profile(request):
    if request.method == 'POST':
        form1 = UserUpdateForm(request.POST, instance=request.user)
        form2 = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.add_message(request, messages.SUCCESS, message='Profile Updated')
            return redirect('profile_page')
        else:
            return HttpResponse('Error Occoured')
    else:
        form1 = UserUpdateForm(instance=request.user)
        form2 = ProfileUpdateForm(instance=request.user.profile)
        return render(request, 'user/UpdateProfile.html', {'form1': form1, 'form2': form2})


@login_required
def room_application(request):
    if request.method == 'POST':
        form = RoomApplicationForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            message = 'Your request has been submitted. You can see your room status in profile section.'
            messages.add_message(request, messages.INFO, message=message)
            return redirect('userhome')
        else:
            messages.add_message(request, messages.WARNING, message='Please tick the checkbox.')
            return redirect('room_apply')
    else:
        if request.user.profile.course is not None:
            if not request.user.profile.apply:
                form = RoomApplicationForm(instance=request.user.profile)
                args = {'form': form}
                return render(request, 'user/RoomApplication.html', args)
            else:
                return HttpResponse('You already applied')
        else:
            messages.add_message(request, messages.WARNING,
                                 message='Kindly update your profile details before apply for room.')
            return redirect('update_profile')


def payment_request_date_expiry(request):
    request_date = request.user.profile.payment_request_date
    expiry_date = timedelta(days=7) + request_date

    if request_date >= expiry_date:
        print('expire')
        increment_signal.connect(receiver=increment_signal_receiver, sender=request.user)
        Profile.objects.filter(id=request.user.profile.id).update(apply=False, payment_request=False, room=None,
                                                                  payment_status='Unpaid')
        messages.add_message(request, messages.INFO, 'Payment duration expired')
        return redirect('userhome')


def next_due(request):
    allocation_date = request.user.profile.room_allocation_date
    next_due_date = allocation_date + timedelta(days=(int(request.user.profile.duration) * 30))
    Profile.objects.filter(id=request.user.profile.id).update(allotted=False, room_expiry_date=next_due_date)


@login_required
def payment_done(request):
    next_due(request)
    Profile.objects.filter(id=request.user.profile.id).update(allotted=True, room_allocation_date=date.today(),
                                                              payment_status='Paid Successfully')
    return redirect('userhome')
