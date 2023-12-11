from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        """
            Provides functionality as seen on twitter/instagram
            handles where user can be searched using '@' symbol prefix
        """
        return f"@{self.username}"
