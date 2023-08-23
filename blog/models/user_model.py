from django.db import models
# from django.contrib.auth.models import AbstractUser



class UserModel(models.Model):
    username = models.CharField(max_length=50)
    # password = models.CharField(max_length=50)
    # email = models.EmailField()
    
    def __str__(self) -> str:
        return self.username