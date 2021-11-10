from django import forms
from django.core.exceptions import ValidationError 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=220)
    password = forms.CharField(max_length=220, widget=forms.PasswordInput)

    def clean(self):
        data = self.cleaned_data

        username = data.get('username')
        password = data.get('password') 

        # optional logic for custom validation
        if len(data) > 5:
            raise ValidationError("Password too short, must be at least five characters.")

        if username == 'gandalf':
            raise ValidationError("You shall not pass!")     

        return data