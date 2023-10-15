from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin



# class CustomeUser(AbstractUser):
#     id_code = models.CharField(max_length=10,null=True, blank=True)
#     mobile = models.CharField(max_length=20,null=True, blank=True)
#     image = models.ImageField(upload_to='users', default='user.jpg')


class CustomeUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email,username, password, **extra_fields)

class CustomeUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomeUserManager()
    
    def __star__(self):
        return self.email
    

class Profile(models.Model):
    user = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    id_code = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='users', default='user.jpg')
    address = models.TextField(null=True, blank=True)


