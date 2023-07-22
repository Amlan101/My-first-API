from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from animeApp.models import AnimeApp
from animeApp.serializers import AnimeAppSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def anime_list(request):
    if request.method == 'GET':
        anime = AnimeApp.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            anime = anime.filter(name_icontains=name)
            
        anime_serializer = AnimeAppSerializer(anime, many=True)
        return JsonResponse(anime_serializer.data, safe=False)
        # safe=False is for objects serialization
        
    elif request.method == 'POST':
        anime_data = JSONParser().parse(request)
        anime_serializer = AnimeAppSerializer(data=anime_data)
        if anime_serializer.is_valid():
            anime_serializer.save()
            return JsonResponse(anime_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(anime_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def anime_detail(request, pk):
    try:
        anime = AnimeApp.objects.get(pk=pk)
    except AnimeApp.DoesNotExist:
        return JsonResponse({'message': 'This anime does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        anime_data = JSONParser().parse(request)
        anime_serializer = AnimeAppSerializer(anime, data=anime_data)
        if anime_serializer.is_valid():
            anime_serializer.save()
            return JsonResponse(anime_serializer.data)
        return JsonResponse(anime_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        anime.delete()
        return JsonResponse({'message': 'Anime was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
     
    