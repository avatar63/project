from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from main_app.models import users, documents
from .serializers import UserSerializer, DocumentSerializer



@api_view(['GET'])
def getData(request):
    Users = users.objects.all()
    serialized = UserSerializer(Users, many=True)
    return Response(serialized.data)


@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("data saved")
    else:
        print("Data not saved")

    return Response(serializer.data)



class DocumentViewSet(ModelViewSet):
    queryset = documents.objects.all()
    serializer = DocumentSerializer