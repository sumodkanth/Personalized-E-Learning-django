from django.urls import path

# import views

from . import views

urlpatterns = [
    path('index/', views.index, name="indexpage"),
    path('index/runcode/', views.runcode, name="runcode"),
    path('coding_answers/', views.Coding_section, name="codinganswers"),
    path('htmlcoding/', views.html_questions, name="htmlcoding"),
    path('phpcoding/', views.php_questions, name="phpcoding"),
    path('htmlanswers/', views.html_answers, name="htmlanswers"),
    path('phpanswers/', views.php_answers, name="phpanswers"),
    path('compile/', views.compile_html, name='compile_html'),
    path('compile-php/', views.compile_php, name='compile_php')
]

