from rest_framework import serializers
from .models import User
from event.models import EventList

class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventList
        fields = ['event_id','title','thumbnail','start_date','end_date','time','location','mode','price','free_event','status',]
class UserSerializer(serializers.ModelSerializer):
    event = EventListSerializer(many=True)
    class Meta:
        model = User
        fields = ['id','user_id','event','first_name','last_name','email','phone','role','is_verified','joined_at','created_at','updated_at']
        read_only_fields = ['id','user_id','joined_at','created_at','updated_at']