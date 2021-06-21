from functools import partial
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .models import Pizza
from .serializers import PizzaSerializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def add_pizza(request):
    if request.method == 'POST':        
        pizza_data = JSONParser().parse(request)
        pizza_serializer = PizzaSerializer(data=pizza_data)
        if pizza_serializer.is_valid():
            pizza_serializer.save()
            return JsonResponse(pizza_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def show_pizza(request):
    if request.method == 'GET': 
        size = request.GET.get('size', None)
        type = request.GET.get('type', None)
        if  type and size:
            all_pizza=Pizza.objects.filter(size__icontains=size).union(Pizza.objects.filter(type__icontains=type))
        elif size and not type:
            all_pizza = Pizza.objects.filter(size__icontains=size)
        elif type and not size:
            all_pizza = Pizza.objects.filter(type__icontains=type)
        else:
            all_pizza=Pizza.objects.all()
        pizza_serializer = PizzaSerializer(all_pizza,many=True) 
        return JsonResponse(pizza_serializer.data,safe=False,status=status.HTTP_200_OK)




@api_view(['GET','PUT','DELETE'])
def update_pizza(request,pk):
    try:
        pizza=Pizza.objects.get(pk=pk)
    except Pizza.DoesNotExist:
        return JsonResponse({'message': 'The pizza with this id does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        pizza_serializer = PizzaSerializer(pizza)
        return JsonResponse(pizza_serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == 'PUT':
        pizza_data = JSONParser().parse(request) 
        pizza_serializer = PizzaSerializer(pizza,data=pizza_data,partial=True) 
        if pizza_serializer.is_valid(): 
            pizza_serializer.save() 
            return JsonResponse(pizza_serializer.data, status=status.HTTP_200_OK) 
        return JsonResponse(pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method=='DELETE':
        pizza.delete()
        return JsonResponse({'message': 'Pizza was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)







