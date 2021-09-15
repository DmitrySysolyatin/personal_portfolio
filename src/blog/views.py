from django.shortcuts import render, get_object_or_404
from .models import Blogs


def all_blogs(request):
    blogs = Blogs.objects.all()
    return render(request, 'all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})
