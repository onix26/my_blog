from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class BlogLIstView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('home')