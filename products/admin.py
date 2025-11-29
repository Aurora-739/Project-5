from django.contrib import admin
from .models import Product, categories

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'display_categories')  # use a method here
    filter_horizontal = ('categories',)

    def display_categories(self, obj):
        """Creates a string of all categories for display in admin list view"""
        return ", ".join([c.name for c in obj.categories.all()])
    display_categories.short_description = 'Categories'

admin.site.register(Product, ProductAdmin)
admin.site.register(categories)
