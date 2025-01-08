from django import forms
from django.forms import ModelForm
from .models import UserHistory

class UserHistoryForm(ModelForm):
    class Meta:
        model = UserHistory
        fields = ['age','height', 'weight', 'gender']