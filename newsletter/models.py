from django.db import models

# Create your models here.
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
