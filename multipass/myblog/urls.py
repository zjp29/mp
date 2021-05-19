from django.contrib import admin
from django.urls import path
  
# importing views from views..py
from .views import blog_view
from .views import personal_view
  
urlpatterns = [
    path('blog', blog_view),
    path('', personal_view),
]