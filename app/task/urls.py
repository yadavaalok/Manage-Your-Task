from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('addevent', CreateEvent.as_view(), name="addevent"),
    path('allevents', ListEvent.as_view(), name="allevents"),
    path('<int:pk>/delete', DeleteEvent.as_view(), name="delete"),
    path('<int:pk>/editevent', UpdateEvent.as_view(), name="editevent"),
]
