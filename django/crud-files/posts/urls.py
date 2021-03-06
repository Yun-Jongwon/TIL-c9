"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


app_name='posts'

urlpatterns = [
    # path('naver/<str:q>/',views.naver),
    # path('github/<str:username>',views.github),
    path('',views.index,name='list'),
    path('create/',views.create,name='create'),
    path('write/',views.new,name='new'),
    path('<int:post_id>/',views.detail,name='detail'),
    path('<int:post_id>/delete/',views.delete,name='delete'),
    path('<int:post_id>/edit/',views.edit,name='edit'),
    path('<int:post_id>/update/',views.update,name='update'),
    path('<int:post_id>/comments/create/',views.comments_create,name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/',views.comments_delete, name='comments_delete'),
    
]
