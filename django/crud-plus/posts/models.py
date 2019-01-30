from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    
    def __str__(self):
        return self.title
    

#Post : Comment = 1:N   
# Foreignkey 는 1:N 중에 N 쪽에 작성
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    #Post에서 가져왔기 때문에 소문자 post로 꼭 써야함 장고에서 정함
    content=models.TextField()
    
    # on_delete 옵션
    #1.CASCADE : 부모가 삭제되면, 자기 자신도삭제.
    #2.PROTECT : 자식이 존재하면, 부모삭제 불가능.
    #3.SET_NULL : 부모가 삭제되면, 자식의 부모 정보를 NULL로 변경
    
    

























#1.Create
#post=Post(title='hello',content='world!')
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