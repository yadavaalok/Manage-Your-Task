from django.urls import path, include
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
]
