from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class blogs(models.Model):
    Authorname = models.CharField(max_length=122)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField()
 
    def __str__(self):
        return self.Authorname