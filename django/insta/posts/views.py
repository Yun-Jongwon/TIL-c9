from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostForm
from .models import Post

def list(request):
    posts=Post.objects.all()
    return render(request, 'posts/list.html',{'posts':posts})


    


# Create your views here.
def create(request):
    if request.method =='POST':
        post_form = PostForm(request.POST, request.FILES) # POST,FILES 순서중요
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
        
    else:
        post_form=PostForm()
    
    return render(request,'posts/create.html',{'post_form':post_form})


def update(request,post_id):
    post=get_object_or_404(Post, id=post_id)
    if request.method =='POST':
        post_form = PostForm(request.POST,request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form=PostForm(instance=post)
    return render(request,'posts/create.html',{'post_form':post_form})



def delete(request, post_id):
    # post=Post.objects.get(id=post_id)
    post=get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('posts:list')
    