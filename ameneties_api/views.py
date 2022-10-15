from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import Food_Serializer,Medicines_Serializer,Other_amenities_Serializer
from .models import Food,medicines,other_amenities

# Create your views here.
class Food_View(APIView):
    def get(self,request):
        food=Food.objects.all()
        serializer=Food_Serializer(food,many=True)
        return Response(serializer.data,status=200)
    def post(self,request):
        serializer=Food_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    def put(self,request,pk):
        food=Food.objects.get(pk=pk)
        serializer=Food_Serializer(food,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
    def delete(self,request,pk):
        food=Food.objects.get(pk=pk)
        food.delete()
        return Response("Food deleted successfully")
class Medicines_View(APIView):
    def get(self,request):
        medicines=medicines.objects.all()
        serializer=Medicines_Serializer(medicines,many=True)
        return Response(serializer.data,status=200)
    def post(self,request):
        serializer=Medicines_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    def put(self,request,pk):
        medicines=medicines.objects.get(pk=pk)
        serializer=Medicines_Serializer(medicines,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
    def delete(self,request,pk):
        medicines=medicines.objects.get(pk=pk)
        medicines.delete()
        return Response("Medicines deleted successfully")
class Other_amenities_View(APIView):
    def get(self,request):
        other_amenities=other_amenities.objects.all()
        serializer=Other_amenities_Serializer(other_amenities,many=True)
        return Response(serializer.data,status=200)
    def post(self,request):
        serializer=Other_amenities_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    def put(self,request,pk):
        other_amenities=other_amenities.objects.get(pk=pk)
        serializer=Other_amenities_Serializer(other_amenities,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
    def delete(self,request,pk):
        other_amenities=other_amenities.objects.get(pk=pk)
        other_amenities.delete()
        return Response("Other amenities deleted successfully")

