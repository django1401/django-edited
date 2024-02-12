from .category import Category
from .trainer import Trainer
from django.db import models
import datetime


class Course(models.Model):
    image = models.ImageField(upload_to='course',default='default.jpg')
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField(default=0)
    teacher = models.ForeignKey(Trainer,on_delete=models.CASCADE)
    counted_views = models.IntegerField(default=0)
    counted_like = models.IntegerField(default=0)
    available_seat = models.IntegerField(default=0)
    schedule = models.DateTimeField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    
    def snip(self):
        return self.content[:20] + '...'
    
    def capt(self):
        return self.title.capitalize()
    