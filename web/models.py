from django.db import models

# Create your models here.
class Contact(models.Model):
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.Fname

   
