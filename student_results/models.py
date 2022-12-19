from django.db import models

class student(models.Model):
    brnch=(
    ("IT","IT"),
    ("CS","CS"),
    ("Civil","Civil"),
    ("Chemical","Chemical")
    )
    yr=(
    ("1st Year","1st Year"),
    ("2nd Year","2nd Year"),
    ("3rd Year","3rd Year"),
    ("4th Year","4th Year")
    )
    s_roll = models.CharField(unique=True,max_length=250)
    s_name = models.CharField(max_length=200, null=True,blank=True, default="full_name")
    branch = models.CharField(max_length=200, choices=brnch,null=True, blank=True, default="Something")
    year = models.CharField(max_length=200,choices=yr, null=True,blank=True, default="1st Year")
    mail = models.EmailField(null=True, blank=True, default="abc@gmail.com")
    mobile = models.IntegerField(null=True,blank=True,default="1234567890")

    def __str__(self):
        return self.s_roll

class result(models.Model):
    brnch=(
    ("IT","IT"),
    ("CS","CS"),
    ("Civil","Civil"),
    ("Chemical","Chemical")
    )
    yr=(
    ("1st Year","1st Year"),
    ("2nd Year","2nd Year"),
    ("3rd Year","3rd Year"),
    ("4th Year","4th Year")
    )
    reg_no= models.ForeignKey(student,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=200, blank=True, default="full_name",null=True)
    branch = models.CharField(max_length=200,choices=brnch,null=True, blank=True, default="IT")
    year = models.CharField(max_length=200, choices=yr,null=True,blank=True, default="1st Year")
    s_marksheet = models.ImageField(upload_to="marksheets", blank=True,null=True)

    def __str__(self):
        return str(self.reg_no)
