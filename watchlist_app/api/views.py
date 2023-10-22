from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Movie
from .serializers import MovieSerializer


#  Create views here....

@api_view(['GET', 'POST'])
def movie_list(request):
    
    movie = Movie.objects.all()
    
    # Use serializer
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    
    # Use serializer
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
    