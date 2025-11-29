from django import forms
from django.core.validators import RegexValidator

phone_validator = RegexValidator(r'^\+?\d{7,15}$',
                                 'Enter a valid phone number.')

class RegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(validators=[phone_validator])
