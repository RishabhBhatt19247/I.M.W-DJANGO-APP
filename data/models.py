from django.db import models

# Create your models here
class Detail(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    date=models.CharField(max_length=10)
    time=models.CharField(max_length=15)
    problem=models.CharField(max_length=50)
    place=models.CharField(max_length=60)
    email=models.EmailField()
    appno=models.IntegerField()
    doctor=models.CharField(max_length=60)
    #this was for returning the string in database 
    #def __str__(self):
        #return "request from :"+self.name+" , application no:"+str(self.appno)+", by: "+self.doctor+", at "+self.time+" ,"+self.date 