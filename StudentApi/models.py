from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    StudentName = models.CharField(max_length=100)
    StudentRollNo = models.IntegerField(primary_key=True)
    StudentBranch = models.CharField(max_length=3)
    StudentGPA = models.FloatField()
    StudentSection = models.CharField(max_length=1)

