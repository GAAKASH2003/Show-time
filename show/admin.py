from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(movie)
admin.site.register(review)
admin.site.register(theatre)
admin.site.register(show)
admin.site.register(booking)
admin.site.register(Rating)

