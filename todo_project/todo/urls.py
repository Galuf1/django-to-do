from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index),
    path('<int:id_query>', views.detail, name='details'),
    path('new/', views.create),
    path('<int:id_query>/edit', views.update, name='edit'),
    path('<int:id_query>/delete', views.delete, name='delete'),


]