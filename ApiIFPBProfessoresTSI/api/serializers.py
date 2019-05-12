from rest_framework import serializers
from .models import Professor


class ProfessorSerializer (serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Professor
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ProfessorSerializer, self).to_representation(instance)
        representation['foto'] = instance.foto.url

        return representation
