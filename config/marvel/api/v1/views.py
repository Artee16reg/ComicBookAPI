from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .marvel_data import comics_list, comic_detail
from .serializers import ComicBookSerializer
from marvel.models import ComicBook


@api_view(['GET'])  # v1/marvel/ or v1/marvel?titleStartsWith=<search word>
def comics_list_view(request):
    """
    List all code comics.
    """
    if request.method == 'GET':
        return Response(comics_list(request))


# Todo add http 'POST' for save comic book to bd
@api_view(['GET', 'POST'])  # v1/marvel<int:pk>
def comic_detail_view(request, pk):
    """
    Detail comic book
    """
    if request.method == 'GET':
        return Response(comic_detail(pk))

    if request.method == 'POST':
        ComicBook.objects.create(title=comic_detail(pk).get('title'))
        ser = ComicBookSerializer()
        return Response(comics_list(request))
