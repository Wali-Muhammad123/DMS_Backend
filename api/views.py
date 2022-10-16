from django.shortcuts import render
import json
from django.http import JsonResponse
from rest_framework.decorators import APIView
from rest_framework.response import Response
from registration_model.serializers import OccupantModelSerializer,FamilyModelSerializer,CampModelSerializer,private_requestSerializer
from registration_model.models import OccupantModel,FamilyModel,CampModel,private_request
class OccupentView(APIView):
    def get(self,request):
        occupent=OccupantModel.objects.all()
        serializer=OccupantModelSerializer(occupent,many=True)
        return Response(serializer.data,status=200)
    def post(self,request):
        serializer=OccupantModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    def put(self,request,pk):
        occupent=OccupantModel.objects.get(pk=pk)
        serializer=OccupantModelSerializer(occupent,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
    def delete(self,request,pk):
        occupent=OccupantModel.objects.get(pk=pk)
        occupent.delete()
        return Response("Occupent deleted successfully")

class FamilyView(APIView):
    def get(self,request):
        family=FamilyModel.objects.all()
        serializer=FamilyModelSerializer(family,many=True)
        return Response(serializer.data,status=200)
    def post(self,request):
        serializer=FamilyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    def put(self,request,pk):
        family=FamilyModel.objects.get(pk=pk)
        serializer=FamilyModelSerializer(family,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
    def delete(self,request,pk):
        family=FamilyModel.objects.get(pk=pk)
        family.delete()
        return Response("Family deleted successfully")
class CampView(APIView):
    def get(self,request):
        camp=CampModel.objects.all()
        serializer=CampModelSerializer(camp,many=True)
        return Response(serializer.data,status=200)
    def post(self,request):
        serializer=CampModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    def put(self,request,pk):
        camp=CampModel.objects.get(pk=pk)
        serializer=CampModelSerializer(camp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
    def delete(self,request,pk):
        camp=CampModel.objects.get(pk=pk)
        camp.delete()
        return Response("Camp deleted successfully")
class request_view(APIView):
    def get(self,request):
        requestt=private_request.objects.all()
        serializer=private_requestSerializer(requestt,many=True)
        return Response(serializer.data,status=200)
    def post(self,request):
        serializer=private_requestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    def put(self,request,pk):
        requestt=private_request.objects.get(pk=pk)
        serializer=private_requestSerializer(requestt,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
    def delete(self,request,pk):
        requestt=private_request.objects.get(pk=pk)
        requestt.delete()
        return Response("Request deleted successfully")