from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:university_id>/', views.university_details, name='university_details'),
    # path('<int:university_id>/update/', views.university_update, name='university_update'),
    path('', views.UniversityListView.as_view(), name='index'),
    path('<int:pk>/', views.UniversityDetailView.as_view(),
         name='university_details'),
    path('<int:pk>/update/', views.UniversityUpdateView.as_view(),
         name='university_update'),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='university/login.html'),
         name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(template_name='university/logout.html'),
         name='logout'),
]
