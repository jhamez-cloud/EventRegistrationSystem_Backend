from rest_framework import serializers
from .models import (EventList,
                     EventDetail,
                     EventAgenda,
                     EventGallery,
                     EventOrganizer,
                     EventSpeakers,
                     EventVenue,
                    )

class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventList
        fields = [
            'id',
            'event_id',
            'title',
            'slug',
            'thumbnail',
            'category',
            'start_date',
            'end_date',
            'time',
            'location',
            'mode',
            'price',
            'currency',
            'free_event',
            'status',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'created_at',
            'updated_at',
            'id',
            ]

        def to_representation(self,instance):
            data = super().to_representation(instance)

            if instance.free_event:
                data['price'] = 0.00
                data.pop('currency',None)

            return data
        
class EventGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventGallery
        exclude = ["event"]


class EventOrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventOrganizer
        exclude = ["event"]


class EventVenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventVenue
        exclude = ["event"]


class EventSpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSpeakers
        exclude = ["event"]


class EventAgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAgenda
        exclude = ["event"]
        
class EventDetailSerializer(serializers.ModelSerializer):
    event = EventListSerializer(read_only=True)

    venue = EventVenueSerializer(read_only=True)

    speakers = EventSpeakerSerializer(
        many=True,
        read_only=True
    )

    organizers = EventOrganizerSerializer(
        many=True,
        read_only=True
    )

    agenda = EventAgendaSerializer(
        many=True,
        read_only=True
    )

    gallery = EventGallerySerializer(
        many=True,
        read_only=True
    )

    available_slots = serializers.ReadOnlyField()

    class Meta:
        model = EventDetail
        fields = [
            "event",
            "description",
            "venue",
            "organizers",
            "speakers",
            "agenda",
            "gallery",
            "tags",
            "capacity",
            "registered",
            "available_slots",
            "created_at",
            "updated_at",
        ]