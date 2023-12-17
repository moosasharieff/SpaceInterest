from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka
from groups.models import Group

# Create your models here.

from django.contrib.auth import get_user_model

# initiating an instance to get user specific data
User = get_user_model()

class Post(models.Model):
    """ Creating schema for storing user's Post data """
    user = models.CharField(User, related_field='posts')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True)

    def __str__(self):
        """ Returns the post which user submitted when calling the object """
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """ Return to the page post submitting the post """
        return reverse('posts:single', kwargs={'username':self.user.username, 'pk':self.pk})

    class Meta:
        """ Posts will be listed in most recent order """
        ordering = ['-created_at']
        unique_together = ['user', 'message'] # connecting user and message uniquely