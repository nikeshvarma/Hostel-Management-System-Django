from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['roll_no', 'date_of_birth', 'temporary_address', 'permanent_address', 'contact_no',
                  'parent_no', 'course', 'profile_pic']

        widgets = {
            'allotted': forms.HiddenInput(),
            'allotted_room': forms.HiddenInput(),
            'apply': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'room': forms.HiddenInput(),
            'room_allocation_date': forms.HiddenInput(),
            'temporary_address': forms.TextInput(attrs={'class': 'form-control'}),
            'permanent_address': forms.TextInput(attrs={'class': 'form-control'}),
            'roll_no': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': DateInput(),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_no': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
        }


class RoomApplicationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['roll_no', 'contact_no', 'duration', 'apply']

        widgets = {
            'duration': forms.Select(attrs={'class': 'form-control w-25'}),
            'roll_no': forms.TextInput(attrs={'class': 'form-control w-25'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control w-25'}),
        }
