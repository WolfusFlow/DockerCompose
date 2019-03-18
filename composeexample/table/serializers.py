from rest_framework import serializers
from table.models import valueTable

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = valueTable
        fields = ('id', 'text', 'value') #'__all__'