from django.urls import path
from .views import *
from accounts.views import project_list,download_project
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('hintro/',htmlintro.as_view(),name='htmlintro'),
    path('basichtml/',basichtml_section,name='basichtml'),
    path('intermediatehtml/',intermediatehtml_section,name='interhtml'),
    path('advancedhtml/',advancedhtml_section,name='advhtml'),
    path('html_learn/',Basiclearn.as_view(),name='bhtml_learn'),
    path('intermediatehtml_learning/',intermediate_text_material,name='ihtml_learn'),
    path('advancedhtml_learning/',advanced_text_material,name='ahtml_learn'),
   
    path('upload2/', upload_project2, name='upload_project2'),
    path('project_list/', project_list, name='project_list'),
    path('download/<int:project_id>/', download_project, name='download_project'),
    path('watch-html-videos/', watch_html_videos, name='watch_html_videos'),
    path('add_comment/<int:video_id>/', add_comment_html, name='add_comment_html'),
    path('toggle_like/<int:video_id>/', toggle_like_html, name='toggle_like_html'),
    path('coursereghtml/', coursereghtml, name='coursereghtml'),
    path('register_html/', register_course_html, name='register_course_html'),
    path('process-payment_html/', process_payment_html, name='process_payment_html'),
    path('puzzle_game_html/', puzzle_game_html, name='puzzle2')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
