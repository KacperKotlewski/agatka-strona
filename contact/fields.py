import django.forms as forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from .models import Mails

class MailingForm(forms.ModelForm):
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'data-size': 'compact',
            }
        ),
        label=False
    )
    names = forms.CharField(
        widget=forms.TextInput(attrs={
                'placeholder': 'Wpisz swoje imię i nazwisko',
            }),
        label = "Imię i nazwisko"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
                'placeholder': 'Twój e-mail',
            }),
        label = "E-Mail"
    )
    topic = forms.CharField(
        widget=forms.TextInput(attrs={
                'placeholder': 'W jakiej sprawie piszesz',
            }),
        label = "Temat"
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
                'placeholder': 'Czego dusza pragnie?',
            }),
        label = "Wiadomość"
    )

    class Meta:
        model = Mails
        fields = ['names', 'email', 'topic', 'message']