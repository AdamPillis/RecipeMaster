from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add_category/', views.add_category, name="add_category"),
    path('update_category/<str:pk_id>/', views.update_category, name="update_category"),
]