# checkout/admin.py
from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemInline,)
    readonly_fields = ('order_number', 'order_total', 'date')
    fields = (
        'order_number',
        'date',
        'full_name',
        'email',
        'address_line1',
        'address_line2',
        'postcode',
        'city',
        'country',
        'order_total',
    )
    list_display = ('order_number', 'date', 'full_name', 'order_total')

admin.site.register(Order, OrderAdmin)
