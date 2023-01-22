from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Package)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(TravellerDetails)