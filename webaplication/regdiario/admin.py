from django.contrib import admin

from .models import Pacient, Phase, Day, Track, Note

# Register your models here.
admin.site.register([Pacient, Phase, Day, Track, Note])
