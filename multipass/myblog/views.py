from django.shortcuts import render
  
# Create your views here.
def blog_view(request):
    return render(request, "index_blog.html")


def personal_view(request):
    return render(request, "index_personal.html")