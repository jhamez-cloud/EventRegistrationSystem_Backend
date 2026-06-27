from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ['user_id','get_events','first_name','last_name','email','phone','role','is_verified']
    search_fields = ['user_id','first_name','last_name','email','phone']
    list_filter = ['role','is_verified']

    @admin.display(description="Events")
    def get_events(self, obj):
        return ", ".join(event.title for event in obj.event.all())