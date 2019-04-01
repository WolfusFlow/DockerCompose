from rest_framework import serializers
from table.models import valueTable

class TableSerializer(serializers.ModelSerializer):
   class Meta:
       model = valueTable
       fields = '__all__'  #('id', 'value', 'created_time')