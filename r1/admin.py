from django.contrib import admin
from django.db.models.base import Model
from .models import myimg

# Register your models here.
admin.site.register(myimg)
class imagadmin(admin.ModelAdmin):
    list_display=['id','img']