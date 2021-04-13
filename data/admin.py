from django.contrib import admin
from data.models import Detail

# Register your models here.

class DetailAdmin(admin.ModelAdmin):
    search_fields=('appno','name','doctor','time','date')
    list_display=['appno','name','doctor','time','date']
    list_filter=['doctor','date']



admin.site.register(Detail,DetailAdmin)
