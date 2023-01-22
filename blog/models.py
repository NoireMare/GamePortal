from django.db import models
from users.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    text = RichTextField()
    image = models.ImageField(upload_to='post_images')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username}: {self.category.name}: {self.title}'


class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.user.username}: {self.id}"



