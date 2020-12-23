from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    msg=models.TextField()
    date=models.DateField()
    def __str__(self):
        retstr=str(self.name)+"( "+str(self.date)+" )"
        return retstr

class Info(models.Model):
    name=models.CharField(max_length=50)
    overview=models.TextField()
    symptoms=models.TextField()
    risk=models.TextField()
    causes=models.TextField()
    prev=models.TextField()
    slug=models.CharField(max_length=130)
    date=models.DateField()
    def __str__(self):
        retstr=str(self.name)+"("+str(self.date)+")"
        return retstr

