from django import forms
from django.contrib.auth.models import User
from main.models import Tweet
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget   
from django.contrib.auth.forms import UserCreationForm
from django import forms                       

class TweetForm(forms.ModelForm):
	class Meta:
		model = Tweet 

class UserCreationForm(forms.ModelForm):

    username = forms.RegexField(label=("Username"), max_length=30, regex=r'^[\w.@+-]+$', help_text = ("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),error_messages = {'invalid': ("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    first_name = forms.CharField(label=("First_name"), max_length=30)
    last_name = forms.CharField(label=("Last_name"), max_length=30)  
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"), widget=forms.PasswordInput, help_text = ("Enter the same password as above, for verification."))
    email = forms.EmailField(label=("Email address"))


    class Meta:
        model = User
        fields = ("username","first_name","last_name","email",)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(("A user with that username already exists."))

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email == "":
            raise forms.ValidationError((""))
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(("The two password fields didn't match."))
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
