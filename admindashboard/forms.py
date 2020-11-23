from user.models import Profile
from django import forms
from hostel.models import Room
from datetime import date


class DateInput(forms.DateInput):
    input_type = 'date'


class AllocationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AllocationForm, self).__init__(*args, **kwargs)
        self.fields['roll_no'].disabled = True
        self.fields['user'].disabled = True
        self.fields['course'].disabled = True
        self.fields['duration'].disabled = True
        self.fields['date_of_birth'].disabled = True
        self.fields['temporary_address'].disabled = True
        self.fields['permanent_address'].disabled = True
        self.fields['contact_no'].disabled = True
        self.fields['parent_no'].disabled = True
        self.fields['apply'].disabled = True
        self.fields['room'].queryset = Room.objects.exclude(capacity=0)

    class Meta:
        model = Profile
        fields = ['user', 'roll_no', 'date_of_birth', 'course', 'contact_no', 'parent_no', 'temporary_address',
                  'permanent_address', 'apply', 'duration', 'room', 'billing_amount', 'payment_request_date',
                  'payment_status', 'payment_request']

        widgets = {
            'allotted_room': forms.Select(attrs={'class': 'form-control'}),
            'apply': forms.CheckboxInput(),
            'duration': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-control'}),
            'temporary_address': forms.TextInput(attrs={'class': 'form-control'}),
            'permanent_address': forms.TextInput(attrs={'class': 'form-control'}),
            'roll_no': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_no': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'room_allocation_date': DateInput(),
            'billing_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_status': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_request_date': DateInput(attrs={'class': 'form-control'})
        }
