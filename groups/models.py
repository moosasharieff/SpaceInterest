from django.db import models
from django.utils.text import slugify

# Create your models here.
import misaka # enables markdown feature
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse

User = get_user_model()
register = template.Library()

class Group(models.Model):
    """ Setting schema for the database """
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        """ rtype : str - Returns the name of the group """
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """ Return URL - 'group:single' after saving data to Group """
        return reverse('group:single', kwargs={'slug':self.slug})

    class Meta:
        """ Ordering the group according group names """
        ordering = ["name"]


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')