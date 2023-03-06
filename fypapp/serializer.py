from rest_framework import serializers
from . models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin
        fields = [ 'adminEmail','adminPassword']

class DirectorEPISerializer(serializers.ModelSerializer):
    class Meta:
        model = directorEPI
        fields = ['directorEPIFirstname', 'directorEPILastname','directorEPIEmail','directorEPIPassword','directorEPIProvince','directorEPIphone','id']
class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = hospital
        fields = ['id', 'hospitalName','hospitalStatus','hospitalCity','hospitalProvince','hospitalAddress','adminId']

class medicalSuperIntendentSerializer(serializers.ModelSerializer):
    class Meta:
        model = medicalSuperIntendent
        fields = ['id', 'medicalSuperIntendentEmail','medicalSuperIntendentPassword','medicalSuperIntendentFirstname','medicalSuperIntendentLastname','phone','hospitalID','hospitalName','adminId']


class vaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = vaccine
        fields = ['id', 'vaccineName','vaccinetype','vaccinequantity','vaccinedescription','adminId']


class childSerializer(serializers.ModelSerializer):
    class Meta:
        model = child
        fields = ['id', 'firstName','lastName','Father_Email','Password','Contact','Mother_CNIC','Father_CNIC','Hospital_Name','Hospital_ID','HCW_ID']

class healthcareworkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = healthcareworker
        fields = ['id', 'Email','Password','firstName','lastName','Contact','directorEPI_ID']

class assignedvaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = assignedvaccine
        fields = ['id', 'HCW_Name','Vaccine_Type','Vaccine_Quantity','Vaccine_Name','directorEPI_ID']
        
class vaccineRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = vaccineRecord
        fields = ['id', 'firstName','lastName','Father_CNIC','Mother_CNIC','Vaccine_ID','Vaccine_Name','Vaccine_Type','Vaccine_Description','HCW_ID']
