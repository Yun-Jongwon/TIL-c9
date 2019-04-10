from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

def list(request):
    posts=Post.objects.order_by('-id').all()
    return render(request, 'posts/list.html',{'posts':posts})


    


@login_required# 함수를 실행하기위해서는 로그인이 되어있어야한다.
def create(request):
    if request.method =='POST':
        post_form = PostForm(request.POST, request.FILES) # POST,FILES 순서중요
        if post_form.is_valid():
            
            post=post_form.save(commit=False)
            post.user=request.user
            
            post.save()# 실제 데이터 베이스에 저장
            return redirect('posts:list')
        
    else:
        post_form=PostForm()
    
    return render(request,'posts/form.html',{'post_form':post_form})


def update(request,post_id):
    post=get_object_or_404(Post, id=post_id)
    if post.user!= request.user:
        return redirect('posts:list')
    if request.method =='POST':
        post_form = PostForm(request.POST,request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect( 'posts:list')
    else:
        post_form=PostForm(instance=post)
    return render(request,'posts/form.html',{'post_form':post_form})



def delete(request, post_id):
    # post=Post.objects.get(id=post_id)
    post=get_object_or_404(Post, id=post_id)
    if post.user!= request.user:
        return redirect('posts:list')
    post.delete()
    return redirect('posts:list')
    