from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='homepage'),
    path('register',views.register,name='register'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('blogdetails',views.blogdetails,name='blogdetails'),
    path('doctors',views.doctors,name='doctor'),
    path('register',views.register,name='register'),
    path('login',views.login,name='log'),
    path('logout',views.logout,name='logout'),
    path('predict',views.predict,name='predict'),
    path('prediction',views.prediction,name='prediction'),

]
