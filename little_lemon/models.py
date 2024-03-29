from django.db import models

# Create your models here.
class Reservations(models.Model):
     reserv = (('1','1 PM'),('2','2 PM'),('3','3 PM'),('4','4 PM'),('5','5 PM'))
     name = models.CharField(max_length=50)
     date = models.DateField(null=True)
     time = models.CharField(max_length=50,choices=reserv,null=True)