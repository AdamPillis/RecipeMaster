from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_desserts, name="recipes"),
    path('<int:pk_id>/', views.full_recipe, name="full_recipe"),
]