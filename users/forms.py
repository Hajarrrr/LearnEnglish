from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
        def save(self, commit=True):
            user = super(UserCreateForm, self).save(commit=False)
            user.extra_field = self.cleaned_data["language"]
            if commit:
                user.save()
            return user