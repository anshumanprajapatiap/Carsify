from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(max_length=30,label='Email')
    def signup(self, request, user):
        user.first_name = self.cleaned_data['firstName']
        user.last_name=self.cleaned_data['last_name']
        user.username=self.cleaned_data['email']
        user.email=self.cleaned_data['email']
        user.save()
        return user

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user','ProfileImg','ContactNo','Address','Email','AddharNumber','PanNumber','VoterID')
