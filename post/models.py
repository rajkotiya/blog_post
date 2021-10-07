from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.db.models.base import Model
from django.db.models.signals import pre_save

class Post(models.Model):
    
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Blog Post',null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=False, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.user)

class PostComment(models.Model):
    
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post =  models.ForeignKey(Post, on_delete=models.CASCADE ,null = True)

    def __str__(self):
        return f'{self.user.get_username()}'



