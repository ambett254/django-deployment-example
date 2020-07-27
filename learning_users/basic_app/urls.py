from django.urls import path
from django.conf.urls import url
from basic_app import views

app_name = "basic_app"

urlpatterns= [
    path('login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register')
]