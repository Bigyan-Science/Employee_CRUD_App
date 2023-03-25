from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    qualification=models.CharField(max_length=50)
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        db_table='Employee'