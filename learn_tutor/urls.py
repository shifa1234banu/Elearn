from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.tsignin, name='tsignin'),
    path('tsignup',views.tsignup,name='tsignup'),
    path('tsignupcheck', views.tsignupcheck, name='tsignupcheck'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('tlogout', views.tlogout, name='tlogout'),
    path('totp',views.totp,name='totp'),
    path('totplogin',views.totplogin,name='totplogin'),
    path('tsendotp',views.tsendotp,name='tsendotp'),
    path('tutorprofile', views.tutorprofile, name='tutorprofile'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('course', views.course, name='course'),
    path('addcourse', views.addcourse, name='addcourse'),
    path('editcourse/<id>', views.editcourse, name='editcourse'),
  
   
   
]