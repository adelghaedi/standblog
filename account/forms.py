from django import forms
from django.contrib.auth.models import User
from django.core.validators import ValidationError
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'input100', "placeholder": _("Username")})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', "placeholder": _("Password")}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if authenticate(username=username, password=password) is None:
            raise ValidationError(_("Incorrect username or password."))


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "input100", "placeholder": _("FirstName")}),
            "last_name": forms.TextInput(attrs={"class": "input100", "placeholder": _("LastName")}),
            "email": forms.EmailInput(attrs={"class": "input100", "placeholder": _("Email")}),
            "username": forms.TextInput(attrs={"class": "input100", "placeholder": _("Username")}),
            "password": forms.PasswordInput(attrs={"class": "input100", "placeholder": _("Password")}),
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "input100", "placeholder": _("FirstName")}),
            "last_name": forms.TextInput(attrs={"class": "input100", "placeholder": _("LastName")}),
            "email": forms.EmailInput(attrs={"class": "input100", "placeholder": _("Email")}),
        }
