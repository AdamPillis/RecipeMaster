from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_desserts, name="recipes"),
    path('<int:pk_id>/', views.full_recipe, name="full_recipe"),
    path('add_recipe/', views.add_recipe, name="add_recipe"),
    path('update_recipe/<str:pk_id>/', views.update_recipe, name="update_recipe"),
]