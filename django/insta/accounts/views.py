from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model,update_session_auth_hash
from .forms import CustomUserChangeForm,ProfileForm,CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method =="POST":
        signup_form=CustomUserCreationForm(request.POST)# usercreationform 디버깅 나올듯
        if signup_form.is_valid():
            user=signup_form.save()
            Profile.objects.create(user=user)# User의 profile생성
            auth_login(request,user)
            return redirect('posts:list')
    else:
        signup_form=CustomUserCreationForm()
    return render(request,'accounts/signup.html',{'signup_form':signup_form})
    
    
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method=='POST':
        login_form=AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            auth_login(request,login_form.get_user())
            return redirect(request.GET.get('next') or'posts:list')
        pass
    else:
        login_form=AuthenticationForm()
    return render(request,'accounts/login.html',{'login_form':login_form})

def logout(request):
    auth_logout(request)
    return redirect('posts:list')



























def people(request,username):
    #get_user_model() => User
    people=get_object_or_404(get_user_model(),username=username)
    return render(request,'accounts/people.html',{'people':people})
    
    
# user edit(회원정보수정)- -user crud중에 u
@login_required
def update(request):
    if request.method == "POST":
        user_change_form=CustomUserChangeForm(request.POST,instance=request.user)
        if user_change_form.is_valid():
            user=user_change_form.save()
            return redirect('people',request.user.username)
    else:
        
        user_change_form=CustomUserChangeForm(instance=request.user)
    return render(request,'accounts/update.html',{'user_change_form':user_change_form})
# user delete-user crud 중에 d
@login_required
def delete(request):
    if request.method =='POST':
        request.user.delete()
        return redirect('posts:list')
    
    return render(request,'accounts/delete.html')



@login_required
def password(request):
    if request.method=='POST':
        password_change_form=PasswordChangeForm(request.user,request.POST)
        if password_change_form.is_valid():
            user=password_change_form.save()
            update_session_auth_hash(request,user)# 비번이 바뀌면서 비번에 의존하던 세션이 사라져서 다시 바뀐 비밀번호 정보로 세션에 보내줌
            return redirect('people',request.user.username)
    else:
        password_change_form=PasswordChangeForm(request.user)
    return render(request, 'accounts/password.html',{'password_change_form':password_change_form})
    
def profile_update(request):
    profile=request.user.profile
    if request.method =='POST':
        profile_form=ProfileForm(request.POST,request.FILES,instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('people',request.user.username)
    else:
        profile_form=ProfileForm(instance=profile)
    return render(request,'accounts/profile_update.html',{'profile_form':profile_form,})




def follow(request,user_pk):
    people=get_object_or_404(get_user_model(),id=user_pk)
    if request.user in people.followers.all():
    # 2. people unfollow하기
        people.followers.remove(request.user)
    else:
    #1.people 을 팔로우 하기
        people.followers.add(request.user)
    
    return redirect('people',people.username)