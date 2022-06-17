from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    user_name = models.CharField(max_length=50, blank=True, default='Anonymous')
    author_email = models.EmailField(blank=True, default='')
    date_time = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}-{self.date_time}")
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    title = models.CharField(max_length=200, blank=True, default='')
    slug = models.SlugField(unique=True, max_length=200)
    user_name = models.CharField(max_length=50, blank=True, default='Anonymous')
    user_email = models.EmailField(blank=True, default='')
    date_time = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    to_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    to_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user_name} {self.content[:30]}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.to_post}-{self.date_time}-{self.content[:30]}")
        if not self.user_name:
            self.user_name = 'Anonymous'
        super(Comment, self).save(*args, **kwargs)
