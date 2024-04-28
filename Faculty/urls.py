from django.urls import path
from .views import *
from django.conf import settings
from Faculty import views
from django.conf.urls.static import static
urlpatterns = [
    path('facultyindex/', views.facultyindex, name='facultyindex'),
    path('videoupload', views.index, name='index'),
    path('add_video/', add_video, name='add_video'),
    path('viewall', views.viewvideos, name='videos'),
    path('delete_video/<int:video_id>/', views.delete_video, name='delete_video'),
    path('comments/', views.comments, name='comments'),
    path('videos/<int:video_id>/', views.video_comments, name='video_comments'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
