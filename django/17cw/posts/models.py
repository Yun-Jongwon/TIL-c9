from django.db import models

# Create your models here.

class Post(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    birthday=models.DateField()
    age=models.IntegerField()
    def __str__(self):
        return self.title
    
#1.Create
#post=Post(title='hello',content='world!')1
#post.save()

#2.Read
#2.1. All
#posts=Post.object.all()

#2.2 Get one
#post=Post.objects.get(pk=1)

#2.3 filter(WHERE)
#조건 맞는것 전부 ( 리스트 형태로 결과가 나옴)
#posts=Post.objects.filter(title='Hello').all()
#첫번째꺼 하나만
#post=Post.objects.filter(title='Hello').first()

#2.4. LIKE
#posts=Post.objects.filter(title__contains="He").all()

#2.5. order_by(정렬),오름차순
#posts=Post.objects.order_by('title').all()
#내림차순
#posts=Post.objects.order_by('-title').all()

#2.6.LIMIT
#Post.objects.all()[:1]

#3.DELTE      
#post=Post.objects.get(pk=2)
#post.title ->2번째
#post.delete()

#4.Update 수정
#post=Post.objects.get(pk=1)
#post.title ->hello
#post.title='hi'
#post.save()
#post=Post.objects.get(pk=1)
#post.title -> hi