from django.urls import path, include
from ..api import views
from . views import WatchDetailAV, WatchListAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    
    path('list/', WatchListAV.as_view, name='watch_list'),
    path('<int:pk>/', WatchDetailAV.as_view, name='watch_details'),
    path('stream/', StreamPlatformAV.as_view, name='stream'),
    path('stream/', StreamPlatformDetailAV.as_view, name='stream-detail')
]
