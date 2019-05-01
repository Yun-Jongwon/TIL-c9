from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list,name='user_list'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    
]
