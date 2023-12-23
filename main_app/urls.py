from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.userRegistration),
    path('email-validation/<str:verification_code>/', views.emailValidation),
    path('login', views.login),
    path('file-download/', views.file_download),
    path('file-upload/', views.file_upload),

]