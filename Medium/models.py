from django.db import models


# Create your models here.
class Book(models.Model):
    Book_Name = models.CharField(max_length=100)
    Author_Name = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    No_of_Pages = models.CharField(max_length=100)


class Register(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Email = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=100)


class Student_Register(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Email = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=100)
