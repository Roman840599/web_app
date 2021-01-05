from django import forms
from django.contrib.auth.forms import UserCreationForm, User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': 'User name'})
        self.fields['password'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': 'Password'})
    username = forms.CharField(max_length=30, min_length=4)
    password = forms.CharField(max_length=20, min_length=8, widget=forms.PasswordInput())

    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get("username")
    #     password = cleaned_data.get("password")
    #     user = authenticate(username=username, password=password)
    #     if not user:
    #         raise forms.ValidationError("Incorrect username or password")
    #     return cleaned_data
