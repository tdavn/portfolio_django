from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    '''Records messages from viewers'''
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
