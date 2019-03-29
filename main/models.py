from django.db import models
from django.urls import reverse

class Content(models.Model):
    fname = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    dob = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(max_length=500, null=True, blank=True)
    about2 = models.TextField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return self.fname + '-' + str(self.id)

    def get_absolute_url(self):
        return reverse('form', kwargs={'pk': self.pk})


class Data(models.Model):
    topic = models.CharField(max_length=100)
    point1 = models.TextField(max_length=500)
    point2 = models.TextField(max_length=500, null=True, blank=True)
    point3 = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.topic

class Skills(models.Model):
    area = models.CharField(max_length=100)
    percentage = models.CharField(max_length=10)

    def __str__(self):
        return self.area




