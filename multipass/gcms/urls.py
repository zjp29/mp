from django.urls import path
from .views import DSListCreate
from . import views

urlpatterns = [
    path('api/gcms/', views.DSListCreate.as_view() ),
]