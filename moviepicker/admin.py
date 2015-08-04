from django.contrib import admin

from moviepicker.models import Movie, Watcher

# Register your models here.
admin.site.register(Movie)
admin.site.register(Watcher)
