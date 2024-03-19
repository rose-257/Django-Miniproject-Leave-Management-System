from django.db import models

# Create your models here.

class student(models.Model):
    Genderchoices = [
         ('M', 'Male'),
         ('F', 'Female')
         ]


    name = models.CharField(max_length=200,null=True)
    age= models.IntegerField()
    email = models.CharField(max_length=200,null=True)
    phone = models.IntegerField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    department=models.CharField(max_length=200,null=True)
    gender = models.CharField(choices=Genderchoices, max_length=10)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200,null=True)
    age= models.IntegerField()
    email = models.CharField(max_length=200,null=True)
    phone = models.IntegerField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    department=models.CharField(max_length=200,null=True)
    loginapproval=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name 

class leaverequest(models.Model):
    student = models.ForeignKey(student,on_delete=models.SET_NULL,related_name= 'student',null=True)
    date = models.DateField()
    days = models.IntegerField()
    reason = models.CharField(max_length=200,null=True)
    leaveapprovalstatus=models.BooleanField(default=False) 
    
    def __str__(self):
        return self.student.name    