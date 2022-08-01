from django.contrib.auth.forms import UserCreationForm
from django import forms

from account.models import Account

class SignupForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = Account
    fields = (
      'username',
      'email',
      'github',
      'password1',
      'password2',
    )

class UserEditForm(forms.ModelForm):
  class Meta:
    model = Account
    fields = (
      'username',
      'email',
      'github',
      'profile_picture',
    )