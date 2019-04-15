from django import forms
from .models import Post,Comment,Image


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['content',]


class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=['file']
        
ImageFormSet=forms.inlineformset_factory(Post,Image,form=ImageForm,extra=3)# parameter (부모 모델, 자식 모델, 여러개로 만들 폼, 폼의 개수)



class CommentForm(forms.ModelForm):
    content= forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'댓글을 작성하세요.'}))
    class Meta:
        model= Comment
        fields=['content']
