from django import forms


class RegistrationForm(forms.Form):
    FirstName = forms.CharField(max_length=50, label='First Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    LastName = forms.CharField(max_length=50, label='Last Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    email = forms.EmailField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ), label='Create New Password', )

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label='Confirm New Password')


class UserAuthenticationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-25'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control w-25'}))
