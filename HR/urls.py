from django.urls import path
from .views import *
from django.conf import settings
from HR import views
from django.conf.urls.static import static
urlpatterns = [
    path('HRindex/', views.applications_list, name='HRindex'),
    path('add-placement/', views.add_placement, name='add_placement'),
    path('placements/', views.placement_list, name='placement_list'),
    path('placements/edit/<int:placement_id>/', views.edit_placement, name='edit_placement'),
    path('placements/delete/<int:placement_id>/', views.delete_placement, name='delete_placement'),
    path('Dashboard/', views.applications_list, name='applications_list')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
