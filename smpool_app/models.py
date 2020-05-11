from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class smservices(models.Model):

    manage= models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    service_desc = models.CharField(max_length=500)
    service_cost = models.FloatField()

    def __str__(self):
        return self.service_desc + ":" + str(self.service_cost)
