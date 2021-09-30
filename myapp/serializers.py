from rest_framework import serializers

class add(serializers.Serializer):
    a = serializers.IntegerField()
    b = serializers.IntegerField()
    