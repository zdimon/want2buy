from django.forms import ModelForm, HiddenInput
from .models import NewAnnouncement
from image_cropping import ImageCropWidget

# Create the form class.
class NewAnnouncementForm(ModelForm):
    class Meta:
        model = NewAnnouncement
        fields = '__all__'
        widgets = {
            'user': HiddenInput()
        }