from django.forms import ModelForm
from .models import Profile

# Create the form class.
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'