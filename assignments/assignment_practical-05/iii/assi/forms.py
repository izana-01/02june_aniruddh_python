from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    confirm_email = forms.EmailField(label='Confirm Email')

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'confirm_email', 'phone', 'age', 'address']

    def clean(self):
        cleaned = super().clean()
        email = cleaned.get('email')
        confirm = cleaned.get('confirm_email')
        if email and confirm and email != confirm:
            self.add_error('confirm_email', 'Emails must match.')
        return cleaned
