from django.urls import path
from . import views

# Create your tests here.


app_name='posts'

urlpatterns=[
    path('',views.list,name='list'),
    path('create/',views.create,name='create'),
    path('<int:post_id>/delete/',views.delete,name='delete'),
    
    
]