from django.contrib import admin
from .models import UserProfile, Country, City, Deparment

admin.site.register(UserProfile)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Deparment)
