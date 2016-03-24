from .models import Note
from rest_framework import serializers


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'content', 'time', 'update_time')