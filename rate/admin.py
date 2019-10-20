from django.contrib import admin
from .models import Currency, Rate

class RateAdmin(admin.ModelAdmin):
    change_list_template = 'admin/rate/custum_change_list.html'



# Register your models here.
admin.site.register(Currency)
admin.site.register(Rate, RateAdmin)