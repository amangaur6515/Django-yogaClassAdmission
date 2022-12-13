from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets 
from rest_framework.views import APIView
from .models import Member 
from .serializers import MemberSerializer
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.decorators import api_view 
import requests
# Create your views here. 

class MemberViewSet(viewsets.ModelViewSet):
    serializer_class=MemberSerializer 
    queryset=Member.objects.all().order_by('id') 

class MemberDetail(APIView):
    def get_object(self,id):
        try:
            return Member.objects.get(id=id)
        except Member.DoesNotExist:
            return None

@api_view(['POST'])
def SaveMember(request):
    if request.method=='POST':
        saveserialize=MemberSerializer(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            return Response(saveserialize.data,status=status.HTTP_201_CREATED)
            
            return render(request,'login.html')
            
def RegisterMember(request):
    if request.method=='POST':
        FullName=request.POST.get('FullName')
        Age=request.POST.get('Age') 
        Gender=request.POST.get('Gender') 
        MobileNo=request.POST.get('MobileNo') 
        Email=request.POST.get('Email') 
        
        Address=request.POST.get('Address') 
        Batch=request.POST.get('Batch') 
        JoiningDate=request.POST.get('JoiningDate') 
        
        data={'FullName':FullName,'Age':Age,'Gender':Gender,
                    'MobileNo':MobileNo,
                    'Email':Email,
                    'Address':Address,
                    'Batch': Batch,
                    'JoiningDate':JoiningDate
        }
        
        saveserialize=MemberSerializer(data=data)
        if saveserialize.is_valid():
            saveserialize.save()
            return render(request,'registrationSuccess.html')
        
        #headers={'Content-Type': 'application/json'} 
        #read=requests.post('http://127.0.0.1:8000/registerapi/',json=data,headers=headers)
        #if read:
            #return render(request,'registrationSuccess.html')
        #else:
            #return render(request,'login.html')

    else:
        return render(request,'register.html') 

def AlreadyMember(request):
    if request.method=='POST':
        MobileNo=request.POST.get('MobileNo')
        try:
            user=Member.objects.get(MobileNo=MobileNo)
        except :
            return render(request,'notFound.html')
        
        id=user.id
        url='/member/'+str(id)
        return redirect(url)
            
        
        
    return render(request,'login.html')

def LoginSuccess(request):
    return render(request,'loginSuccess.html')


