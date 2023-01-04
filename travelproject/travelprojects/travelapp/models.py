from django.db import models

class travel(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pic')
    des=models.TextField()


    def __str__(self):
        return self.name

class person(models.Model):
    Image=models.ImageField(upload_to='pic')
    des=models.TextField()



