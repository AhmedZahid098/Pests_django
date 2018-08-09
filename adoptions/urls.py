from django.urls import path
from adoptions import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adoptions/<int:id>/', views.pet_detail, name='pet_detail'),
]
