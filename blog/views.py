from django.views.generic import CreateView
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content',)
    success_url = 'homepage.html'
