from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from base.models import Advocate,Company

from base.serializers import AdvocateSerializer, CompanySerializer

@api_view(['GET'])
def endPoints(request):
    data = [
        '/advocates',
        'addAdvocate/',
        'advocates/:username',
    ]
    return Response(data)

class AdvocatesList(APIView):
    
    def get(self,request):
        query = request.GET.get('query')
        print("QUERY:",query)
        
        if query == None:
            query = ""
        advocates = Advocate.objects.filter(
            Q(username__icontains=query) | 
            Q(bio__icontains = query )
            )
        serializer = AdvocateSerializer(advocates,many=True)

        return Response(serializer.data)
    
    # create an advocate
    def post(self,request):
        advocate = Advocate.objects.create(
        username = request.data["username"],
        bio = request.data["bio"]
        )
        serializer = AdvocateSerializer(advocate, many=False)

        return Response(serializer.data)






# @api_view(['GET','POST'])
# def advocates_list(request):
#     # http://127.0.0.1:8000/advocates/?query=salvin
#     # add an advocate
#     if request.method == "POST":
#         advocate = Advocate.objects.create(
#         username = request.data["username"],
#         bio = request.data["bio"]
#         )
#         serializer = AdvocateSerializer(advocate, many=False)

#         return Response(serializer.data)
    
#     # get all the advocates
#     if request.method == 'GET':
#         query = request.GET.get('query')
#         print("QUERY:",query)
        
#         if query == None:
#             query = ""
#         advocates = Advocate.objects.filter(
#             Q(username__icontains=query) | 
#             Q(bio__icontains = query )
#             )
#         serializer = AdvocateSerializer(advocates,many=True)

#         return Response(serializer.data)
    
class AdvocateDetail(APIView):

    # get object
    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise JsonResponse("Advocate dosen't exist!!",safe = False)


    # get the advocate : 
    def get(self, request, username):
        advocate = self.get_object(username=username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def put(self, request,username):
        advocate = self.get_object(username=username)

        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()

        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    
    def delete(self, request,username):
        advocate = self.get_object(username=username)
        advocate.delete()
        return Response("user deleted successfully !!")




# @api_view(['GET','PUT','DELETE'])
# def advocate_detail(request,username):
#     advocate = Advocate.objects.filter(username=username).first()

#     if request.method == 'GET':
        
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
#         advocate.save()

#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response('user deleted successfully!!')

class CompanyList(APIView):
    def get(self,request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True) 
        return Response(serializer.data)

    def post(self,request):
        company = Company.objects.create(
            name = request.data['name'],
            bio = request.data['bio']
        )
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data)
