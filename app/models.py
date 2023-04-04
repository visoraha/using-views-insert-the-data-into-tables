from django.db import models

# Create your models here.
class Course(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=100)
    tname=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.cname
class Student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=100)
    cid=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.sname
class Exam(models.Model):
    sid=models.ForeignKey(Student,on_delete=models.CASCADE)
    marks=models.IntegerField()
    def __str__(self) -> str:
        return str(self.marks)