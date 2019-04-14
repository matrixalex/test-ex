from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class PostInfo(models.Model):
    def setData(self,post:Post):
        self.postId = post.id
        self.post = post