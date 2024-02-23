from django import forms
from d1.models import *


class Diaryform(forms.ModelForm):
    class Meta:
        model=Diary
        fields='__all__'