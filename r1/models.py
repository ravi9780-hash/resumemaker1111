from django.db import models

# Create your models here.
class myimg(models.Model):
    img=models.ImageField(upload_to='profile/')
    
    def __str__(self) -> str:
        return self.img
