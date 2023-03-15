from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .marvel_data import comics_list


@api_view(['GET'])
def comics_list_view(request):
    """
    List all code comics.
    """
    if request.method == 'GET':
        return Response(comics_list(request))
