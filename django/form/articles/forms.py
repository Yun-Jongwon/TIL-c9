from django import forms
from .models import Article

class ArticleForm(forms.Form):
    title = forms.CharField(label='제목')
    content=forms.CharField(label='내용',widget=forms.Textarea(attrs={
        'rows':5,
        'cols':50,
        'placeholder':'내용을입력하세요',
    }))
    
    
class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(label='제목')
    #이게 meta보다 우선순위가 높음(오버라이드)
    class Meta:
        model = Article
        fields=['title','content']