from django import forms
from .models import Oneline, Reply

class OnelineForm(forms.ModelForm):
    rating = forms.FloatField(max_value=5, min_value=0)

    class Meta:
        model = Oneline
        fields = ('content', 'rating')

class ReplyForm(forms.ModelForm):
    content = forms.CharField(min_length=2, label='', widget=forms.TextInput(attrs={'placeholder': '댓글'}))
    class Meta:
        model = Reply
        fields = ('content', )
        labels = {
            'content': '댓글 입력'
        }

        
        