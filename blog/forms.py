from django import forms
from django.core.validators import ValidationError
from .models import Message


class ContactUsForm(forms.Form):
    BIRTH_YEAR_RANGE = ["2020", "2021", "2022"]
    COLOR_CHOICES = [
        ("red", "RED"),
        ("pink", "PINK"),
        ("blue", "BLUE"),
    ]

    birth_year = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "mb-4"}, years=range(1900, 2009)))
    name = forms.CharField(max_length=12, label="Your name", required=False)
    message = forms.CharField(max_length=10, label="Your Message")
    colors = forms.ChoiceField(widget=forms.CheckboxSelectMultiple(attrs={"class": "row"}), choices=COLOR_CHOICES, )

    def clean(self):
        name = self.cleaned_data.get("name")
        print(name)
        message = self.cleaned_data.get("message")

        if name == message:
            raise ValidationError(
                "name and message can not be same..."
            )

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control","placeholder":"Enter a title"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter a email"}),
            "body":forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter your body"}),
        }
