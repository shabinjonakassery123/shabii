from django.db import models

class reg(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.IntegerField()

class registration(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=250)
    phone = models.IntegerField()

class empreg(models.Model):
    username = models.CharField(max_length=50)
    password = models.IntegerField()

class empreg1(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    qualification = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    phone = models.IntegerField()


class admintest(models.Model):
    username = models.CharField(max_length=100)
    password = models.IntegerField()

class custpost(models.Model):
    text = models.CharField(max_length=230)