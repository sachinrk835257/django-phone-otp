from django.urls import path, include
from otpauth import views

urlpatterns = [
    # path('login/',views.login_page, name="go to app1.urls"),
    path('signup/',views.signup,name='go to signup'),
    path('otp/<token>',views.phone_otp_verify,name='verify the otp'),
    path('logout/',views.logout_page,name='go to logout.urls'),
]