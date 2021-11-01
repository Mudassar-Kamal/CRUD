from django import forms
from .models import User


class StudentRegistraion(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control'})
