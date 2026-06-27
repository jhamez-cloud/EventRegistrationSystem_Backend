from event.models import EventList,EventDetail
from event.serializers import EventListSerializer,EventDetailSerializer
from config.viewsets import StandardViewset

class EventListViewset(StandardViewset):
    queryset = EventList.objects.all()
    serializer_class = EventListSerializer

class EventDetailViewset(StandardViewset):
    queryset = EventDetail.objects.all()
    serializer_class = EventDetailSerializer