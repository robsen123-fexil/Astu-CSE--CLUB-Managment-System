from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('posts/<str:pk>/', views.posts , name ='posts'),
    path('adminpage/',views.adminpage , name='adminpage'),
    path('registeruser/' , views.registeruser, name ='registeruser')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)