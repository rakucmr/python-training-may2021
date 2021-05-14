from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:university_id>/', views.university_details, name='university_details'),
    # path('<int:university_id>/update/', views.university_update, name='university_update'),
    path('', views.UniversityListView.as_view(), name='index'),
    path('<int:pk>/', views.UniversityDetailView.as_view(),
         name='university_details'),
    path('<int:pk>/update/', views.UniversityUpdate.as_view(),
         name='university_update'),
]
