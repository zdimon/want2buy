from django import forms

class OfferForm(forms.Form):
    desc = forms.CharField(widget=forms.Textarea, required=True)
    username = forms.CharField()
    price = forms.CharField(required=True)
    url = forms.CharField(required=False)
    email = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    register = forms.BooleanField(required=False)
    file = forms.FileField(required=False)
    announcement_id = forms.CharField(widget=forms.HiddenInput)

    def save(self):
        data = self.cleaned_data
        print(data)