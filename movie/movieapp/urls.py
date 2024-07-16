from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
     path('clear_registration_success/', views.clear_registration_success, name='clear_registration_success'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('category/<str:category_name>/', views.category_view, name='category'),
    path('search/', views.movie_search, name='movie_search'),
    path('movie/update/<int:pk>/', views.update_movie, name='update_movie'),
    path('movie/delete/<int:pk>/', views.delete_movie, name='delete_movie'),
    ]
