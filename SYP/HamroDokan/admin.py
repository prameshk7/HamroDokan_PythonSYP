from django.contrib import admin
from .models import productmodel,ordermodel,profilemodel
from django.contrib.auth.models import Group

admin.site.site_header = 'HamroDokan Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'location','description')
    list_filter = ['location']

# Register your models here.
admin.site.register(productmodel, ProductAdmin)
admin.site.register(ordermodel)
admin.site.register(profilemodel)
# admin.site.unregister(Group)