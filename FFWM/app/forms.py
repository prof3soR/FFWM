from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['username', 'name', 'email', 'spotify_playlist', 'instagram_link', 'password']
