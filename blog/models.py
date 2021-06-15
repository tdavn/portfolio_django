from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

# Create your models here.


class BlgCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))  # id is the same as pk
        return reverse('blg_index')


class BlgPost(models.Model):
    title = models.CharField(max_length=255, default='title here')
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=255) # optionally leave out default value
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BlgCategory, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=400)
    body = RichTextUploadingField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    # likes = models.ManyToManyField(User, related_name='blog_posts')

    # def total_likes(self):
    #     return self.likes.count()

    def __str__(self):
        return self.title + ' | by ... ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))  # id is the same as pk
        return reverse('blg_index') # redirect to home instead of the content of the post
