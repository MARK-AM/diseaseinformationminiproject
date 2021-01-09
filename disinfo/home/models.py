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
    img=models.ImageField(default="")
    slug=models.CharField(max_length=130)
    date=models.DateField()
    def __str__(self):
        retstr=str(self.name)+"("+str(self.date)+")"
        return retstr

class News(models.Model):
    title=models.CharField(max_length=50,default="")
    content=models.TextField(default="")
    link=models.TextField(default="")
    img1= models.ImageField(default="")
    date=models.DateField()
    def __str__(self):
        retstr=str(self.title)
        return retstr


