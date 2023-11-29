from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from ablog.models import Blog, Comment, Likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def blog_list(request):
    return render(request, 'ablog/blog_list.html',context={})

class CreateBlog(CreateView):
    model = Blog
    template_name = 'ablog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image',)


