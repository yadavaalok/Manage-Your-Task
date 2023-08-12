from django.urls import path
from .views import *
from accounts.views import Logout, Profile


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('addevent', CreateEvent.as_view(), name="addevent"),
    path('allevents/<str:event_type>', ListEventByType.as_view(), name="allevents"),
    path('eventstatus/<str:event_status>', ListEventByStatus.as_view(), name="eventstatus"),
    path('<int:pk>/delete', DeleteEvent.as_view(), name="delete"),
    path('<int:pk>/editevent', UpdateEvent.as_view(), name="editevent"),
    path('logout', Logout.as_view(), name="logout"),
    path('profile', Profile.as_view(), name='profile'),
]
