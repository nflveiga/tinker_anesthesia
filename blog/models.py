from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    photo = models.ImageField(upload_to='post_images', blank=True, null=True)
    title = models.CharField(max_length=100)
    intro= models.TextField()
    text = RichTextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
