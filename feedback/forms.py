# -*- coding: utf-8 -*-
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size': '40', 'class': 'required',
                                                                            'placeholder': u'Тема', 'name': 'name',
                                                                            'aria-required': True}))
    sender = forms.EmailField(
        widget=forms.HiddenInput(attrs={'size': '40', 'class': 'required email', 'type': 'email',
                                        'placeholder': 'E-mail'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': u'Сообщение',}))

    def __init__(self, *args, **kwargs):
        logined = kwargs.pop('logined')
        super(ContactForm, self).__init__(*args, **kwargs)
        if logined:
            del self.fields['sender']
