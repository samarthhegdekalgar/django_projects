from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CategorySerializer, GuestSerializer
from .models import Category, Guest
from rest_framework import status
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Welcome</h1>')


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def api_category_view(request, pk=None):

    if request.method == 'GET' and pk is not None:
        try:
            category = Category.objects.get(type=pk)
        except Category.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    if request.method == 'GET' and pk is None:
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    if request.method == 'PUT':
        try:
            category = Category.objects.get(type=pk)
        except Category.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        else:
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status.HTTP_200_OK)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        try:
            category = Category.objects.get(type=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            operation = category.delete()
            data = {}
            if operation:
                data["message"] = "Delete Successful"
            else:
                data["message"] = "Delete Failed"
            return Response(data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        pass



@api_view(['GET', ])
def api_guests_list_view(request):
    guest = Guest.objects.all()
    if request.method == 'GET':
        serializer = GuestSerializer(guest, many=True)
        return Response(serializer.data)
