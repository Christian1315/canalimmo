from django.shortcuts import render

# Create your views here.

def showBlogPage(request):
    return render(request,'blog.html')

def showBlogDetail(request):
    return render(request,'blog-detail.html')