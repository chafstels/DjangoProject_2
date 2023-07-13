from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title[:50]}'

    class Meta:
        ordering = ['create_at']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post.title[:25]} --> {self.comment[:50]}'
