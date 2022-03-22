from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import fields
from django.forms.widgets import PasswordInput
from django.contrib.auth import authenticate # for check from database



class Register(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    Retype_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

    def clean(self):
        super().clean() ###for all the constructor allready in form inherit the feature
        p=self.cleaned_data.get('password')
        p1=self.cleaned_data.get('Retype_password')
        if p!=p1:
            raise forms.ValidationError("both passwords did not match")    




class logform(forms.Form):
    username=forms.CharField(max_length=100,help_text="user name")
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)
    def clean(self):
        u=self.cleaned_data.get("username")
        p=self.cleaned_data.get("password")
        ur=authenticate(username=u,password=p)
        if ur==None:
            raise ValidationError("user does not exist")

        

                