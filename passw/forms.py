from django.forms import ModelForm
from .models import Password

class PasswordForm(ModelForm):
    class Meta:
        model = Password
<<<<<<< HEAD
        fields = "username", "password", "url"
=======
        fields = "password", "username", "url"
>>>>>>> 0b50ab174f8487bfb9251c38ae057b0dab5d2f96
