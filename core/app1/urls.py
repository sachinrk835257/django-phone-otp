from django.urls import path, include
from app1 import views

urlpatterns = [
    path('',views.index, name="go to app1.urls"),
    path('auth/',include('otpauth.urls'),name='go to otpauth.urls')
]