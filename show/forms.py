from .models import *
from django import forms
from typing import Any, Dict
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from django import forms


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')
        
    def __init__(self, *args, **kwargs):
      super(UserCreateForm, self).__init__(*args, **kwargs)

      for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
             
          

class Reviewform(forms.ModelForm):
    content=forms.CharField(label='',widget=forms.Textarea(attrs={'rows':5, 'cols':57}))
    class Meta:
        model=review
        fields=('content',)
        

class TicketForm(forms.ModelForm):
    num_ticket=forms.IntegerField(min_value=1,max_value=2,label='Number of tickets')
    
    class Meta:
        model=booking
        fields = ('name','num_ticket','seat_no')
    
        
