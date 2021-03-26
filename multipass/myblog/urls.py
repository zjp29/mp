from django.contrib import admin
from django.urls import path
  
# importing views from views..py
from .views import blog_view
  
urlpatterns = [
    path('', blog_view),
]