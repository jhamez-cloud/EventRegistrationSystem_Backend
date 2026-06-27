from django.contrib import admin
from unfold.admin import ModelAdmin,StackedInline,TabularInline
from .models import (
    EventDetail,
    EventList,
    EventVenue,
    EventSpeakers,
    EventAgenda,
    EventGallery,
    EventOrganizer,
)

class VenueInline(StackedInline):
    model = EventVenue
    extra = 0
    max_num = 1


class SpeakerInline(StackedInline):
    model = EventSpeakers
    extra = 1
    max_num = 1


class AgendaInline(TabularInline):
    model = EventAgenda
    extra = 1


class GalleryInline(TabularInline):
    model = EventGallery
    extra = 1


class OrganizerInline(TabularInline):
    model = EventOrganizer
    extra = 1

@admin.register(EventList)
class EventListAdmin(ModelAdmin):
    list_display = (
        "title",
        "slug",
        "thumbnail",
        "category",
        "start_date",
        "end_date",
        "time",
        "location",
        "mode",
        "price",
    )

@admin.register(EventDetail)
class EventDetailAdmin(ModelAdmin):
    inlines = [
        VenueInline,
        SpeakerInline,
        AgendaInline,
        GalleryInline,
        OrganizerInline,
    ]

    list_display = (
        "event",
        "capacity",
        "registered",
        "tags",
        "available_slots",
        "created_at",
    )