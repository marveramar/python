from django.urls import path
from django.urls import path  
from . import views

urlpatterns = [
    path('project', views.projects, name="project"),
    path('product/<str:pk>/', views.product, name="product")
]

