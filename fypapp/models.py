from django.db import models

# Create your models here.
class admin(models.Model):
    adminEmail=models.CharField(max_length=15)
    adminPassword=models.CharField(max_length=15)
    
class child(models.Model):
    id=models.IntegerField(primary_key=True)
    firstName=models.CharField(max_length=25)
    lastName=models.CharField(max_length=25)
    Father_Email=models.CharField(max_length=25)
    Password=models.CharField(max_length=500)
    Contact=models.IntegerField()
    Father_CNIC=models.IntegerField()
    Mother_CNIC=models.IntegerField()
    Hospital_Name=models.CharField(max_length=500)
    Hospital_ID=models.IntegerField()
    HCW_ID=models.IntegerField()


class feedback(models.Model):
    feedbackID=models.IntegerField()
    msg=models.CharField(max_length=100)
    userID=models.IntegerField()

class hospital(models.Model):
    id=models.IntegerField(primary_key=True)
    hospitalName=models.CharField(max_length=25)
    hospitalStatus=models.CharField(max_length=15)
    hospitalCity=models.CharField(max_length=25)
    hospitalProvince=models.CharField(max_length=25)
    hospitalAddress=models.CharField(max_length=25)
    adminId=models.IntegerField()

class healthcareworker(models.Model):
    id=models.IntegerField(primary_key=True)
    Email=models.CharField(max_length=15)
    Password=models.CharField(max_length=15)
    firstName=models.CharField(max_length=25)
    lastName=models.CharField(max_length=25)
    Contact=models.IntegerField()
    directorEPI_ID=models.IntegerField()

class medicalSuperIntendent(models.Model):
    id=models.IntegerField(primary_key=True)
    medicalSuperIntendentEmail=models.CharField(max_length=15)
    medicalSuperIntendentPassword=models.CharField(max_length=15)
    medicalSuperIntendentFirstname=models.CharField(max_length=25)
    medicalSuperIntendentLastname=models.CharField(max_length=25)
    phone=models.CharField(max_length=15)
    hospitalID=models.IntegerField()
    hospitalName=models.CharField(max_length=25)
    adminId=models.IntegerField()

class sigin(models.Model):
    tokenID=models.IntegerField()
    userID=models.IntegerField()
    time=models.DateTimeField()

class vaccine(models.Model):
    id=models.IntegerField(primary_key=True)
    vaccineName=models.CharField(max_length=15)
    vaccinetype=models.CharField(max_length=15)
    vaccinequantity=models.CharField(max_length=15)
    vaccinedescription=models.CharField(max_length=15)
    adminId=models.IntegerField()

class directorEPI(models.Model):
    directorEPIFirstname=models.CharField(max_length=25)
    directorEPILastname=models.CharField(max_length=25)
    directorEPIEmail=models.CharField(max_length=15)
    directorEPIPassword=models.CharField(max_length=15)
    directorEPIProvince=models.CharField(max_length=25)
    directorEPIphone=models.IntegerField()
    id=models.IntegerField(primary_key=True) 

class accesslevel(models.Model):
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    access=models.CharField(max_length=25)

class assignedvaccine(models.Model):
    id=models.IntegerField(primary_key=True)
    HCW_Name=models.CharField(max_length=25)
    Vaccine_Type=models.CharField(max_length=25)
    Vaccine_Quantity=models.IntegerField()
    Vaccine_Name=models.CharField(max_length=25)
    directorEPI_ID=models.IntegerField()


class vaccineRecord(models.Model):
    id=models.IntegerField(primary_key=True)
    firstName=models.CharField(max_length=15)
    lastName=models.CharField(max_length=15)
    Father_CNIC=models.IntegerField()
    Mother_CNIC=models.IntegerField()
    Vaccine_ID=models.IntegerField()
    Vaccine_Name=models.CharField(max_length=15)
    Vaccine_Type=models.CharField(max_length=15)
    Vaccine_Description=models.CharField(max_length=15)
    HCW_ID=models.IntegerField()