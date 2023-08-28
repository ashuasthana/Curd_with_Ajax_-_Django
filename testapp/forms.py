from django import forms
from .models import StudentRagistration

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=StudentRagistration
        fields='__all__'
        widgets = {
    'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name_id', 'autocomplete': 'name'}),
    'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email_id', 'autocomplete': 'email'}),
    'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password_id',  'autocomplete': 'off'}),
}