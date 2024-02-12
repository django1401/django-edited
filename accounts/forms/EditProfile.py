from django import forms
from ..models import Profile

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'user','first_name', 'last_name', 'image', 'phone', 'address']