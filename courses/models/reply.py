from django.db import models
from .comment import Comment


class Reply(models.Model):
    which_comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name