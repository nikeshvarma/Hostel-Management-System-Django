from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F, Q
from django.shortcuts import render, redirect
from .forms import *
from django.dispatch import Signal

decrement_signal = Signal(providing_args=['pk'])
increment_signal = Signal(providing_args=['username'])


def decrement_signal_receiver(sender, **kwargs):
    Room.objects.filter(room_id=Profile.objects.get(user_id=kwargs['pk']).room.room_id).update(
        capacity=F('capacity') - 1)


def increment_signal_receiver(sender, **kwargs):
    Room.objects.filter(room_id=Profile.objects.get(user__username=kwargs['username']).room.room_id).update(
        capacity=F('capacity') + 1)


@login_required
def student_table(request):
    profiles = Profile.objects.filter(user__is_superuser=False, allotted=True)
    args = {'profiles': profiles}
    return render(request, 'admin/HostelStudentTable.html', args)


@login_required
def user_table(request):
    profiles = Profile.objects.filter(user__is_superuser=False)
    return render(request, 'admin/RegisterUsersTable.html', {'UserProfile': profiles})


@login_required
def room_request(request):
    user = Profile.objects.filter(apply=True, payment_request=False, user__is_superuser=False)
    args = {'requests': user}
    return render(request, 'admin/RoomRequests.html', args)


@login_required
def room_allocation(request, pk):
    if request.method == 'POST':
        decrement_signal.connect(receiver=decrement_signal_receiver, sender=request.user)
        user = Profile.objects.get(user_id=pk)
        form = AllocationForm(request.POST, instance=user)
        if form.is_valid() and user.payment_request:
            form.save()
            decrement_signal.send(sender=request.user, pk=pk)
            return redirect('room_request_page')
        else:
            messages.add_message(request, messages.WARNING, message='Please Tick The Checkbox.')
            return redirect('allocation_page', pk)
    else:
        form = AllocationForm(instance=Profile.objects.get(user_id=pk))
        args = {'form': form, 'user': pk}
        return render(request, 'admin/AllocationPage.html', args)


@login_required
def search(request):
    if request.method == 'POST':
        data = request.POST['search']
        result = Profile.objects.filter(Q(user__first_name=data) |
                                        Q(user__last_name=data) |
                                        Q(user__email=data) |
                                        Q(roll_no=data))
        return render(request, 'admin/RegisterUsersTable.html', {'UserProfile': result})
    else:
        return redirect('user_table_page')


@login_required
def reject_application(request, pk):
    Profile.objects.filter(user_id=pk).update(apply=False)
    return redirect('room_request_page')


@login_required
def view_profile(request, username):
    args = {'user': Profile.objects.get(user__username=username)}
    return render(request, 'admin/ApplicationForm.html', args)


@login_required
def delete_account(request, username):
    increment_signal.connect(receiver=increment_signal_receiver, sender=request.user)
    user = User.objects.filter(username=username)
    try:
        increment_signal.send(sender=request.user, username=username)
        user.delete()
        return redirect('user_table_page')
    except AttributeError:
        user.delete()
        return redirect('user_table_page')
