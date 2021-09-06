from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('update/<str:pk>/',views.Update_task,name='update'),
    path('delete/<str:pk>/',views.delete_task,name='delete'),
]