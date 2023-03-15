from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .marvel_data import comics_list, comic_detail


@api_view(['GET'])
def comics_list_view(request):
    """
    List all code comics.
    """
    if request.method == 'GET':
        return Response(comics_list(request))


@api_view(['GET'])
def comic_detail_view(request, pk):
    """
    Detail comic book
    """
    if request.method == 'GET':
        return Response(comic_detail(pk))
