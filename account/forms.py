from django.forms import ModelForm
from .models import Profile
from image_cropping import ImageCropWidget

# Create the form class.
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'avatar': ImageCropWidget,
        }