from django import forms
from main.models import Tweet
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget                          

class TweetForm(forms.ModelForm):
	class Meta:
		model = Tweet 

BIRTH_YEAR_CHOICES = ('1990','1980', '1981', '1982')
GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'))
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
                            ('green', 'Green'),
                            ('black', 'Black'))

class RegisterForm(forms.Form):
    
    name = forms.CharField(widget= forms.TextInput(attrs={'class':'special'}))
    email = forms.EmailField(required=True)
    Password = forms.CharField(required=True, widget=forms.TextInput(attrs={'size':'40'}))
    user = forms.CharField(widget= forms.TextInput())