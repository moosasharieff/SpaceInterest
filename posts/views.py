from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()

class PostList(SelectRelatedMixin, generic.ListView):
    """
    Connecting the model for Posts and adding relationship between 'user' and 'group'
    """
    model = models.Post
    select_related = ('user', 'group')

class UserPosts(generic.ListView):
    """
    Viewing all the posts of a specific user is list form
    """
    model = models.Post
    template_name = "post/user_post_list.html"

    def get_queryset(self):
        """
        Querying database for a specific user and fetching all the posts of his.
        """
        try:
            # checking if user exists and fetching its posts
            self.post.user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

     def get_context_data(self, *args, **kwargs):
         context = super().get_context_data(**kwargs)
         context['post_user'] = self.post_user
         return context
