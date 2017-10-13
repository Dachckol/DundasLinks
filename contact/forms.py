from django import forms
from django.forms import ModelForm
from contact.models import ContactEntry, Type


class ContactForm(ModelForm):
    name = forms.CharField(label=(u'Name'))
    email = forms.EmailField(label=(u'Email Address'))
    contentType = forms.ModelChoiceField(Type.objects)
    content = forms.CharField(
        label=(u'Details'), widget=forms.Textarea())

    class Meta:
        model = ContactEntry
        exclude =('answered',)