from django.urls import path

from . import views

urlpatterns = [
    path('', views.adsignin, name='adsignin'),
    path('adsignincheck', views.adsignincheck, name='adsignincheck'),
    path('adhome', views.adhome, name='adhome'),
    path('user',views.user,name='user'),
    path('blockuser/<id>',views.blockuser,name='blockuser'),
    path('unblockuser/<id>',views.unblockuser,name='unblockuser'),
    path('category', views.category, name='category'),
    path('addcategory', views.addcategory, name='addcategory'), 
    path('editcategory/<id>', views.editcategory, name='editcategory'),
    path('categorycheck/<id>',views.categorycheck,name='categorycheck'),
   
   
   
   
]