from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import PostForm,CommentForm,ImageFormSet
from .models import Post,Comment
from django.db import transaction

def list(request):
    posts=Post.objects.order_by('-id').all()
    comment_form=CommentForm()
    return render(request, 'posts/list.html',{'posts':posts,'comment_form':comment_form})


    


@login_required# 함수를 실행하기위해서는 로그인이 되어있어야한다.
def create(request):
    if request.method =='POST':
        post_form = PostForm(request.POST) # POST,FILES 순서중요
        image_formset=ImageFormSet(request.POST, request.FILES)# hidden 에서 value값 받아와야함
        if post_form.is_valid() and image_formset.is_valid():
            
            post=post_form.save(commit=False)
            post.user=request.user
            
            with transaction.atomic(): # db에 요청을 보내고 속도가 느려서 저장 안된 상태에서 다음 코드가 실행될수 도 있기 때문에 순서대로 돌아가도록 해주는 역할
            #첫번째
                post.save()# 실제 데이터 베이스에 저장
                # 두번째
                image_formset.instance=post
                image_formset.save() # 실제 데이터베이스에 저장
            
            return redirect('posts:list')
        
    else:
        post_form=PostForm()
        image_formset=ImageFormSet()
    
    return render(request,'posts/form.html',{'post_form':post_form,'image_formset':image_formset})

@login_required
def update(request,post_id):
    post=get_object_or_404(Post, id=post_id)
    if post.user!= request.user:
        return redirect('posts:list')
    if request.method =='POST':
        post_form = PostForm(request.POST, instance=post)
        image_formset=ImageFormSet(request.POST,request.FILES,instance=post)
        if post_form.is_valid() and image_formset.is_valid():
            post_form.save()
            image_formset.save()
            return redirect( 'posts:list')
    else:
        post_form=PostForm(instance=post)
        image_formset=ImageFormSet(instance=post)
    return render(request,'posts/form.html',{'post_form':post_form,'image_formset':image_formset})


@login_required
def delete(request, post_id):
    # post=Post.objects.get(id=post_id)
    post=get_object_or_404(Post, id=post_id)
    if post.user!= request.user:
        return redirect('posts:list')
    post.delete()
    return redirect('posts:list')
    
    
    
    
    
@login_required
@require_POST
def comment_create(request,post_id):
    comment_form=CommentForm(request.POST)
    if comment_form.is_valid():
        comment=comment_form.save(commit=False)
        comment.user=request.user
        comment.post_id=post_id
        comment.save()
    
    return redirect('posts:list',)
    
    
@require_http_methods(['GET','POST'])
def comment_delete(request,post_id, comment_id):
    comment=get_object_or_404(Comment, id=comment_id)
    if comment.user!= request.user:
        return redirect('posts:list')
    comment.delete()
    return redirect('posts:list')
@login_required
def like(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    
    if request.user in post.like_users.all():
    # 좋아요 취소
        post.like_users.remove(request.user)
    else:# 좋아요 !
        post.like_users.add(request.user)       
    
    return redirect('posts:list')