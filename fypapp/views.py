from django.shortcuts import render
from . models import *
from . serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class postdata(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        data = request.POST.dict()
                        serializer = UserSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(status=status.HTTP_200_OK)

class SIGNIN(APIView):
    def post(self,request):
        if request.method=='POST':
            data=request.POST.dict()
            email=data['email']
            hi=accesslevel.objects.filter(email=email).first()
            if hi.password==data['password']:
                return Response(status=status.HTTP_200_OK,data=hi.access)
     
            return Response(status=status.HTTP_404_NOT_FOUND)

class savedirectorEPI(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        accessleve=accesslevel()
                        data = request.POST.dict()
                        serializer = DirectorEPISerializer(data=data)
                        email=data['directorEPIEmail']
                        password=data['directorEPIPassword']
                        access=data['access']
                        accessleve.email=email
                        accessleve.password=password
                        accessleve.access=access
                        if serializer.is_valid():
                            serializer.save()
                            accessleve.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            return Response(status=status.HTTP_404_NOT_FOUND)

class showdirectorEPI(APIView):

    def get(self, request):
        if request.method=='GET':
            directorEP = directorEPI.objects.all().order_by('id')
            serializer = DirectorEPISerializer(directorEP, many=True)

            return Response(serializer.data)


class countdirectorEPI(APIView):

    def get(self, request):
        if request.method=='GET':
            directorEP = directorEPI.objects.count()
            return Response(directorEP)

class savehospital(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        data = request.POST.dict()
                        serializer = HospitalSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            return Response(status=status.HTTP_404_NOT_FOUND)
class showhospital(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = hospital.objects.all().order_by('id')
            serializer = HospitalSerializer(EP, many=True)

            return Response(serializer.data)

class counthospital(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = hospital.objects.count()
            return Response(EP)


class savemedicalSuperIntendent(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        data = request.POST.dict()
                        accessleve=accesslevel()
                        serializer = medicalSuperIntendentSerializer(data=data)
                        email=data['medicalSuperIntendentEmail']
                        password=data['medicalSuperIntendentPassword']
                        access=data['access']
                        accessleve.email=email
                        accessleve.password=password
                        accessleve.access=access
                        if serializer.is_valid():
                            serializer.save()
                            accessleve.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            return Response(status=status.HTTP_404_NOT_FOUND)
class showmedicalSuperIntendent(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = medicalSuperIntendent.objects.all().order_by('id')
            serializer = medicalSuperIntendentSerializer(EP, many=True)

            return Response(serializer.data)

class countmedicalSuperIntendent(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = medicalSuperIntendent.objects.count()
            return Response(EP)
            
class savevaccine(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        data = request.POST.dict()
                        serializer = vaccineSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            return Response(status=status.HTTP_404_NOT_FOUND)
                            
class showvaccine(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = vaccine.objects.all().order_by('id')
            serializer = vaccineSerializer(EP, many=True)

            return Response(serializer.data)

class countvaccine(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = vaccine.objects.count()
            return Response(EP)

class savechild(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        data = request.POST.dict()
                        serializer = childSerializer(data=data)
                        accessleve=accesslevel()
                        email=data['Father_Email']
                        password=data['Password']
                        access=data['access']
                        accessleve.email=email
                        accessleve.password=password
                        accessleve.access=access
                        if serializer.is_valid():
                            serializer.save()
                            accessleve.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            return Response(status=status.HTTP_404_NOT_FOUND)
                            
class showchild(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = child.objects.all().order_by('id')
            serializer = childSerializer(EP, many=True)

            return Response(serializer.data)


def searchchild(self, request):
        if request.method=='GET':
            EP = child.objects.all().order_by('id')
            serializer = childSerializer(EP, many=True)

            return Response(serializer.data)
class countchild(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = child.objects.count()
            return Response(EP)

class savehealthcareworker(APIView):
        def post(self, request):
                if request.method=="POST": 
                        data = request.POST.dict()
                        accessleve=accesslevel()
                        serializer = healthcareworkerSerializer(data=data)
                        email=data['Email']
                        password=data['Password']
                        access=data['access']
                        accessleve.email=email
                        accessleve.password=password
                        accessleve.access=access
                        if serializer.is_valid():
                            serializer.save()
                            accessleve.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            return Response(status=status.HTTP_404_NOT_FOUND)
                            
class showhealthcareworker(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = healthcareworker.objects.all().order_by('id')
            serializer = healthcareworkerSerializer(EP, many=True)

            return Response(serializer.data)

class counthealthcareworker(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = healthcareworker.objects.count()
            return Response(EP)

class saveassignedvaccine(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        data = request.POST.dict()
                        serializer = assignedvaccineSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            return Response(status=status.HTTP_404_NOT_FOUND)
                            
class showassignedvaccine(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = assignedvaccine.objects.all().order_by('id')
            serializer = assignedvaccineSerializer(EP, many=True)

            return Response(serializer.data)

class countassignedvaccine(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = assignedvaccine.objects.count()
            return Response(EP)

class savevaccineRecord(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        data = request.POST.dict()
                        serializer = vaccineRecordSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            return Response(status=status.HTTP_404_NOT_FOUND)
                            
class showvaccineRecord(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = vaccineRecord.objects.all().order_by('id')
            serializer = vaccineRecordSerializer(EP, many=True)

            return Response(serializer.data)

class countvaccineRecord(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = vaccineRecord.objects.count()
            return Response(EP)

class updatevaccineRecord(APIView):

         def put(self, request):
                data = request.data
                try:
                        i=data['id']
                        q = vaccineRecord.objects.get(id=i)
                        q.id=data['updateid']
                        q.save()
                        so= vaccineRecord.objects.get(id=i)
                        so.delete()
                        return Response(status=status.HTTP_200_OK)
                except:
                        print("id is not updating")
                        try:
                            i=data['id']
                            q = vaccineRecord.objects.get(id=i)
                            q.firstName=data['updatefirstName']
                            q.save()
                            return Response(status=status.HTTP_200_OK)
                        except:
                            print("firstName is not updating")
                            try:
                                i=data['id']
                                q = vaccineRecord.objects.get(id=i)
                                q.lastName=data['updatelastName']
                                q.save()
                                return Response(status=status.HTTP_200_OK)
                            except:
                                print("lastName is not updating")
                                try:
                                    i=data['id']
                                    q = vaccineRecord.objects.get(id=i)
                                    q.Father_CNIC=data['updateFather_CNIC']
                                    q.save()
                                    return Response(status=status.HTTP_200_OK)
                                except:
                                 print("Father_CNIC is not updating")
                                 try:
                                    i=data['id']
                                    q = vaccineRecord.objects.get(id=i)
                                    q.Mother_CNIC=data['updateMother_CNIC']
                                    q.save()
                                    return Response(status=status.HTTP_200_OK)
                                 except:
                                  print("Mother_CNIC is not updating")
                                  try:
                                    i=data['id']
                                    q = vaccineRecord.objects.get(id=i)
                                    q.Vaccine_ID=data['updateVaccine_ID']
                                    q.save()
                                    return Response(status=status.HTTP_200_OK)
                                  except:
                                   print("Vaccine_ID is not updating")
                                   try:
                                    i=data['id']
                                    q = vaccineRecord.objects.get(id=i)
                                    q.Vaccine_Name=data['updateVaccine_Name']
                                    q.save()
                                    return Response(status=status.HTTP_200_OK)
                                   except:
                                    print("Vaccine_Name is not updating")
                                    try:
                                        i=data['id']
                                        q = vaccineRecord.objects.get(id=i)
                                        q.Vaccine_Type=data['updateVaccine_Type']
                                        q.save()
                                        return Response(status=status.HTTP_200_OK)
                                    except:
                                     print("Vaccine_Type is not updating")
                                     try:
                                        i=data['id']
                                        q = vaccineRecord.objects.get(id=i)
                                        q.Vaccine_Description=data['updateVaccine_Description']
                                        q.save()
                                        return Response(status=status.HTTP_200_OK)
                                     except:
                                      print("Vaccine_Description is not updating")
                                      try:
                                        i=data['id']
                                        q = vaccineRecord.objects.get(id=i)
                                        q.HCW_ID=data['updateHCW_ID']
                                        q.save()
                                        return Response(status=status.HTTP_200_OK)
                                      except:
                                       print("HCW_ID is not updating")



class deletevaccineRecord(APIView):

    def delete(self, request):
               try:
                data = request.data
                id=data['id']
                q = vaccineRecord.objects.get(id=id)
                q.delete()
                return Response(status=status.HTTP_200_OK)
               except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
    