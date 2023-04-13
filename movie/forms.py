from django import forms
from .models import Movie

class MovieSearchForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': '영어로 입력해주세요. English Only'}))
    class Meta:
        model = Movie
        fields = ('title', )