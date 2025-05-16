from rest_framework import serializers

from .models import NatoMember

class NatoMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NatoMember
        fields = '__all__'
        read_only_fields = ('id','slug')
