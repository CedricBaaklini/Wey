from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserManager

from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = UserManager
        fields = ('email', 'name', 'password1', 'password2')
