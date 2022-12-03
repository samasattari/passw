from django.forms import ModelForm
from .models import Password

class PasswordForm(ModelForm):
    class Meta:
        model = Password
        fields = "username", "password", "url"