#backend/post/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200) # title 컬럼
    content = models.TextField()             # content 컬럼

    def __str__(self):
        """A string representation of the model."""
        return self.title