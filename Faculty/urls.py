from django.urls import path
from .views import *
from django.conf import settings
from Faculty import views
from django.conf.urls.static import static
urlpatterns = [
    path('facultyindex/', views.facultyindex, name='facultyindex'),

    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
