from django.db import models

# Create your models here.
class Dept(models.Model):
    deptid = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=100,unique=True)
    deptloc=models.CharField(max_length=100)


    def __str__(self):
        return str(self.deptid)



class Emp(models.Model):
    emp_id = models.IntegerField(primary_key=True)  # User-provided emp_id
    #serial_no = models.AutoField(primary_key=True)  # Auto-generated serial number
    emp_name = models.CharField(max_length=100)   
    emp_sal = models.DecimalField(max_digits=10, decimal_places=2)
    job = models.CharField(max_length=100)
    hire_date = models.DateField()
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    coomition = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deptid = models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name

        
class Sal_grade(models.Model):
    grade=models.IntegerField(primary_key=True)
    lowsal=models.DecimalField(max_digits=10,decimal_places=2)
    highsal=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return str(self.grade)        