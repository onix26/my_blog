from django.views.generic import ListView,DetailView
from .models import Post


class BlogLIstView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'detail.html'