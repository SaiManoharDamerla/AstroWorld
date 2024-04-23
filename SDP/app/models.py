from django.db import models


# Create your models here.

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, blank=False)
    email = models.CharField(max_length=50, unique=True, blank=False)
    password = models.CharField(max_length=15, blank=False)
    details = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Register_table"


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, blank=False)
    email = models.CharField(max_length=50, blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Contact_table"


class Userdetails(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, unique=True, blank=False)
    email = models.CharField(max_length=50, unique=True, blank=False)
    fname = models.CharField(max_length=25, blank=False)
    lname = models.CharField(max_length=25, blank=False)
    address = models.TextField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=50, blank=False)
    postalcode = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = "Userdetails_table"

    def __str__(self):
        return self.username
