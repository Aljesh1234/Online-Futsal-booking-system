from django.db import models

# Create your models here.

class FutsalBooking(models.Model):
    username =models.CharField(max_length=50)
    email = models.EmailField()
    mblnumber = models.IntegerField()
    futsal_choice = models.CharField(max_length=50)
    date = models.DateField()
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.username
