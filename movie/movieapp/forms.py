from django import forms
from django.contrib.auth.models import User
from .models import Movie, Review, Profile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].widget = forms.NumberInput(attrs={'max': 10, 'min': 1})
