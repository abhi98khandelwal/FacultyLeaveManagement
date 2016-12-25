"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_Details(models.Model):
    user = models.OneToOneField(User,related_name='details')
    department = models.CharField(max_length = 50)
    medical = models.PositiveSmallIntegerField(default=10)
    casual = models.PositiveSmallIntegerField(default=8)
    earned = models.PositiveSmallIntegerField(default=3)
    study = models.PositiveSmallIntegerField(default=15)
    holiday = models.PositiveSmallIntegerField(default=3)
    faculty = models.BooleanField(default=0)
    hod = models.BooleanField(default = 0)
    registrar = models.BooleanField(default = 0)
    director = models.BooleanField(default =0)
    work_holiday = models.FloatField(default = 0)

    def add_earned_leaves(self):
        if self.work_holiday >0:
            self.earned+=(self.work_holiday/2.5)
        self.work_holiday = 0



class Leave_Status(models.Model):
    leave_choices = [('medical',"Medical Leave"),('earned',"Earned Leave"),('casual',"Casual Leave"),('holiday',"Restricted Holiday Leave"),('study',"Study Leave")] 
    user= models.TextField(blank=True)
    type = models.CharField(choices = leave_choices,max_length = 7,default = 'earned')
    start_date = models.DateField()
    end_date = models.DateField()
    suggested = models.CharField(max_length = 50)
    status = models.BooleanField(default=False)