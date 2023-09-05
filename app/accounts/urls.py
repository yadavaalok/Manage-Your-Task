from django.urls import path
from .views import *


urlpatterns = [
    path('register', Register.as_view(), name="register"),
    path('', Login.as_view(), name="login"),
    path('reset', ResetPassword.as_view(), name="reset"),
    path('update_profile/<int:pk>', UpdateUser.as_view(), name='update_profile'),
]
