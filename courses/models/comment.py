from django.db import models
from .course import Course


class Comment(models.Model):
    which_course = models.ForeignKey(Course,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
    