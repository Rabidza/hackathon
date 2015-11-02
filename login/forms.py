#forms.py
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"))
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("Fool me once shame on me, fool me twice shame on you..."))
 
    def clean(self):
        if 'password' in self.cleaned_data:
            return self.cleaned_data

    def first_name(self):
        return self.cleaned_data