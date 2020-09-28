from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns=[
    path('',views.index),
    path('allreview/',views.review),
    path('signup/',views.signup),
    path('login/',views.login),
    path('aftersignup/',views.aftersignup),
    path('afterlogin/',views.afterlogin),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)