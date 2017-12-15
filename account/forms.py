from django.forms import ModelForm, HiddenInput, TextInput
from .models import Profile
from image_cropping import ImageCropWidget

# Create the form class.
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'avatar': ImageCropWidget,
            'user': HiddenInput()
            #'first_name': TextInput(attrs={'require': True})
        }