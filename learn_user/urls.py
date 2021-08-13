from django.urls import path,include

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signupcheck', views.signupcheck, name='signupcheck'),
    path('registerotp',views.registerotp, name='registerotp'),
    path('logout', views.logout, name='logout'),
    path('otplogin', views.otplogin, name='otplogin'),
    path('sendotp', views.sendotp, name='sendotp'),
    path('otphtml', views.otphtml, name='otphtml'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('coursedetails/<id>/',views.coursedetails,name='coursedetails'),
    path('add_cart',views.add_cart,name='add_cart'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('remove_cart_item/<id>',views.remove_cart_item,name='remove_cart_item'),
    path('search',views.search,name='search'),
    path('categorycourse/<id>/',views.categorycourse,name='categorycourse'),
    path('stripe',views.stripe,name='stripe'),
    path('invoice',views.invoice,name='invoice'),
    path('editcheck/<id>/',views.editcheck,name='editcheck'),
    path('edit/<id>/',views.edit,name='edit'),
    path('allcourse',views.allcourse,name='allcourse'),
]