from rest_framework import serializers
from main_app.models import users, documents
from rest_framework.serializers import Serializer, FileField

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'
        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = documents
        fields='__all__'