from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms



User = get_user_model()
class CreateUserForm(UserCreationForm):

    username = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'required': 'True',
            'verbose_name':'Lietotāvārds',
            'class' : 'reg'
        }),
    )


    password1 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'required': 'True',
            'class' : 'reg'
        }),
    )

    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'required': 'True',
            'class' : 'reg'
        }),
    )
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'required': 'True',
            'verbose_name':'Vārds',
            'class' : 'reg'
        }),
    )

    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'required': 'True',
            'verbose_name':'Uzvārds',
            'class' : 'reg'
        }),
    )

    email = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'required': 'True',
            'verbose_name':'Uzvārds',
            'class' : 'reg'
        }),
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']