from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import User, EmailVerification
import uuid
from django import forms


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'youplay-input', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'youplay-input', 'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'youplay-input', 'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'youplay-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'youplay-input', 'placeholder': 'Password check'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'youplay-input', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email']

    # def save(self, commit=True):
    #     user = super(UserRegistrationForm, self).save(commit=True)
    #
    #     return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'youplay-input', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'youplay-input', 'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'youplay-input', 'placeholder': 'Username', 'readonly': True}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'youplay-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'youplay-input', 'placeholder': 'Password check'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'youplay-input', 'placeholder': 'Email', 'readonly': True}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'youplay-input'}), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'image']


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'youplay-input', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'youplay-input', 'placeholder': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'password']
