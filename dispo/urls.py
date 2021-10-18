from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/create/', views.create_user),
    path('post/create/', views.create_post),
    path('users/top/', views.get_user),
    path('users/feed/<user_id>/', views.get_post),
    # Add remaining endpoints here
]
