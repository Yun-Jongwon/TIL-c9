from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    
# 정리
# class Post: django ->model이라 부름
#             DB -> Table이라 부름
# post = Post() : django -> instance or object, DB-> record or row
# title: django->field, db-> column
    
    
# CRUD
# 1. Create
# 방법1
# post=Post(title='hello-1')
# post.save()

# 방법2
# post2=Post.objects.create(title='hello-2')

# 방법3
# post3=Post()
# post3.title='hello-3'
# post3.save()

# 2. Read
# 2-1.All
# posts=Post.objects.all()

# 2-2. one
# Post.objects.get(id=1)
# Post.objects.get(id=1).title # get은 같은것이 여러개 있으면 id 값이작은것부터 다 나옴

# Post.objects.get(title='hello-2')
# get_object_or_404(Post,title='hello-2')

# Post.objects.filter(pk=1)[0]
# Post.objects.filter(pk=1).first()

# 2-3. where(filter)
# posts=Post.objects.filter(title='hello-1')  => queryset 형태로 나옴
# post=Post.objects.filter(title='hello-1').first()

# 2-4 Like
# posts=Post.objects.filter(title__contains='lo')


# sort(order_by)
#  Post.objects.order_by('title')
#  Post.objects.order_by('-title')
# Post.objects.filter(title__contains='lo').order_by('-id') => 실행된 시점에서 정렬(order_by를 먼저 부르고 다른 메소드 부르면 정렬된 상태에서 다른 메소드 실행됨)


# offset & limit 시험

# limit는 갯수
# post=Post.objects.all()[0] => 데이터베이스에서 offset 0 limit 1  인 역할
# post=Post.objects.all()[1] => 데이터베이스에서 offset 1 limit 1  인 역할
# Post.objects.all()[1:3] => offset 1 limit 2
# Post.objects.all()[offset:offset+limit] 


# 3. update
# post1= Post.objects.get(pk=1)
# post1.title='hello-5'
# post1.save()

# 4.Delete
# post1= Post.objects.get(pk=1)
# post1.delete()
 