from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('email', views.forget, name="forget"),
    path('password/reset/confirm/<str:uid>/<str:token>',
         views.reset_pass, name="reset"), #passowrd reset url
    path('activate/<str:uid>/<str:token>',
         views.active_email, name="active_email"), #email activation url
     path('google/',views.redirectSocial,name="socialgoogle"),
     path('facebook/',views.redirectSocialfacebook,name="socialfacebook"),
     path('stripe/',views.stripee,name='stripe'),
     path('charge/', views.charge, name="charge"),
     path('success/<str:args>',views.success,name='success'),
]
