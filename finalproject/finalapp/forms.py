from django import forms
from.models import Movie,Review
from django import forms
from django.contrib.auth.models import User

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'poster', 'desc', 'date', 'actors', 'genere', 'link']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating','user']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email']

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)

