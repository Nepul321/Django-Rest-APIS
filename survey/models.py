from django.db import models

class Submission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField('email')
    favorite_color = models.CharField(max_length=20)
    bio = models.TextField()