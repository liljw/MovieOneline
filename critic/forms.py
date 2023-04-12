from django import forms
from .models import Oneline, Reply

class OnelineForm(forms.ModelForm):

    class Meta:
        model = Oneline
        fields = '__all__'

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = '__all__'
        