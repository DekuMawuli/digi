from django.contrib import admin
from .models import BusSeat, Bus, Driver, Branch, BranchBuses

admin.site.register(BusSeat)
admin.site.register(Bus)
admin.site.register(Driver)
admin.site.register(Branch)
admin.site.register(BranchBuses)
