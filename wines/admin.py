from django.contrib import admin

# Register your models here.

from .models import Wine, Grape


class GrappeAdmin(admin.ModelAdmin):
	fields = ['name', 'type']


class WineAdmin(admin.ModelAdmin):
	fieldsets = [
		("Basic Data",{'fields': ["name", "vineyard", "year", "type", "country", "image", "rating"]}),
		("Notes",{'fields': ["notes"]})
	]

admin.site.register(Wine, WineAdmin)
admin.site.register(Grape, GrappeAdmin)