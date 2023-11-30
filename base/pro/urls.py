from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login_view'),
   
    path('home/', views.home, name='home'),
    path('posts/<str:pk>/', views.posts , name ='posts'),
    path('adminpage/',views.adminpage , name='adminpage'),
    path('registeruser/' , views.registeruser, name ='registeruser'),
    path('delete_users/', views.delete_users, name='delete_users'),
    path('user_info/', views.user_info, name='user_info'),
    path('add_event/', views.add_event, name='add_event'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('postlist/', views.post_list, name='post_list'),
    path('delete_selected_posts/', views.delete_selected_posts, name='delete_selected_posts'),
    path('dashboard/', views.dashboard, name='dashboard')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)