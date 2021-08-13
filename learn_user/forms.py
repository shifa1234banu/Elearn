from django import forms
from .models import Profile




   
class ImageForm(forms.ModelForm):
    userimage = forms.ImageField(required=False, error_messages={'invalid':("Image file only")}, widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ['userimage',]


