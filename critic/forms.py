from django import forms
from .models import Oneline, Reply

class OnelineForm(forms.ModelForm):
    rating = forms.FloatField(max_value=5, min_value=0)

    class Meta:
        model = Oneline
        fields = ('content', 'rating')

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ('content', )
        
        