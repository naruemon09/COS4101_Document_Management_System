from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(blank=False, max_length=150, verbose_name='first name')
    last_name = models.CharField(blank=False, max_length=150, verbose_name='last name')
    email = models.EmailField(blank=False, unique=True, max_length=254, verbose_name='email address', error_messages={'unique': 'A user with that email address already exists.'})
    phone = models.CharField(blank=False, max_length=10, verbose_name='phone')
    position = models.CharField(blank=False, max_length=50, verbose_name='position')

class Department(models.Model):
    # variable names come from the class diagram
    departmentName = models.CharField(max_length=100, primary_key=True)
    buildingName = models.CharField(max_length=100)

    def __str__(self):
        return self.departmentName

class Document(models.Model):
    # variable names come from the class diagram
    documentID = models.CharField(max_length=100, primary_key=True)
    subject = models.CharField(max_length=100)
    fileDocument = models.BinaryField()
    date = models.DateField()
    sender = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='recipient')
    annotation = models.TextField()
    status = models.CharField(max_length=100)

    # added `type` because the class diagram doesn't have "ประเภทเอกสาร" but the design draft has.
    type = models.CharField(max_length=100)

    # if True, the document is at the receiving end. Otherwise, the sending end.
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    
