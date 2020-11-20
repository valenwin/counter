from django.urls import path

from core import views

urlpatterns = [
    path('', views.ImagesListView.as_view(), name='images'),
    path('image/<str:slug>/', views.ImageDetailView.as_view(), name='image_details'),

]
