from django.shortcuts import render, redirect
from .models import Post 

# Create your views here.

# def throw
# def catch

def new(request):
    return render(request,'new.html')
    
    
def create(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    birthday=request.POST.get('birthday')
    age=request.POST.get('age')
    
    post=Post(name=name,email=email,birthday=birthday,age=age)
    post.save()
    
    return redirect(f'/posts/{post.pk}/')
    
    
    
    
    
    
        
def index(request):
    # All Post
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})
    
    
    
def detail(request, post_id):
    post=Post.objects.get(pk=post_id)
    return render(request,'detail.html',{'post':post})
    
    
    
    
    
def delete(request, post_id):
    #삭제하는 코드
    post=Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/posts/')
    
    


def edit(request,post_id):
    post=Post.objects.get(pk=post_id)
    return render(request,'edit.html',{'post':post})
    

def update(request,post_id):
    #수정하는 코드
    post=Post.objects.get(pk=post_id)
    post.name=request.POST.get('name')
    post.email=request.POST.get('email')
    post.birthday=request.POST.get('birthday')
    post.age=request.POST.get('age')
    post.save()
    
    return redirect(f'/posts/{post.id}/')


    
    
    
    
    
# def naver(request, q):
    
#     return redirect(f'https://search.naver.com/search.naver?query={q}')
    
    
# def github(request,username):
#     return redirect(f'https://github.com/{username}')