from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)

class OrderShow(admin.ModelAdmin):
    list_display = ['productName','orderedBy']
    class Meta:
        model = Order

admin.site.register(Order, OrderShow)
admin.site.register(Tag)