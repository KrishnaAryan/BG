from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'mobile', 'email', 'location', 'message']


from django import forms
from .models import Leads

from django import forms

class LeadsForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = ['name', 'mobile', 'email']
