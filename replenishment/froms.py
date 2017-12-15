from django.forms import ModelForm
from replenishment.models import Replanishment


class ReplanishmentForm(ModelForm):
    class Meta:
        model = Replanishment
        fields = ['amount']
