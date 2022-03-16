from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django import forms
from app.models import *



class AuditorForm(ModelForm):
    class Meta:
        model = Auditor
        fields = '__all__'


class BronForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].required = False
        self.fields['auditor'].required = False
        
    class Meta:
        model = Bron
        fields = ['auditor', 'date', 'start_time',
         'end_time', 'comment', 'user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form__input2'}),
        }
    

class CorpusForm(ModelForm):
    class Meta:
        model = Corpus
        fields = '__all__'

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={}))
