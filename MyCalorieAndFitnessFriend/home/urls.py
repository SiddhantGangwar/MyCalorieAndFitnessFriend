from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('bmi',views.bmi,name='bmi'),
    path('user', views.index, name="index"),
    path('delete/<int:id>/', views.delete_consume, name="delete"),
]