from django.urls import path
from . import views

urlpatterns = [
    path('addtask/', views.addtask, name='addtask'),
    path('markasdone/<int:pk>/', views.markasdone, name='markasdone'),
    path('markasundone/<int:pk>/', views.markasundone, name='markasundone'),
    path('edittask/<int:pk>', views.edittask, name='edittask'),
    path('deletetask/<int:pk>/', views.deletetask, name='deletetask'),
]