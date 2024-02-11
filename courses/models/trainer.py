from django.db import models
from .skill import Skills
from accounts.models import CustomeUser

class Trainer(models.Model):
    info = models.ForeignKey(CustomeUser , on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    description = models.TextField()
    image = models.ImageField(upload_to='trainer', default='teacher.png')
    twitter = models.CharField(max_length=255, default='#')
    facebook = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    linkdin = models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info.email
    