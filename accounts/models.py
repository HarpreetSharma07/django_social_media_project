from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):

#auth.models.User has inbuilt username
    def __str__(self):
        return "@{}".format(self.username)
