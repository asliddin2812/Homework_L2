from rest_framework import serializers

from .models import NatoMember

class NatoMemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NatoMember
        fields = ('id','name','joined_year','capital_city','slug')
        read_only_fields = ('id','slug')

class NatoMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NatoMember
        fields = '__all__'
        read_only_fields = ('id','slug')
