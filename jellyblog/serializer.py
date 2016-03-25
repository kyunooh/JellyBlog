from .models import Note
from rest_framework import serializers, viewsets, routers


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'content', 'time', 'update_time')


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


router = routers.DefaultRouter()
router.register(r'users', NoteViewSet)