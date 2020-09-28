from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns=[
    path('',views.index),
    path("home/",views.home),
    path('login/',views.login),
    path('afterlogin/',views.afterlogin),
    path('signup/',views.signup),
    path('contact/',views.contact),
    path('aftersignup/',views.aftersignup),
    path('forgot/',views.forgot),
    path('logout/',views.logout),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)