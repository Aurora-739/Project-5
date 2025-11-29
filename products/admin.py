from django.contrib import admin
from .models import Product, Category

# Custom admin for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price', 'rating', 'display_categories')
    filter_horizontal = ('categories',)  # for ManyToManyField

    def display_categories(self, obj):
        """Returns a comma-separated list of categories for admin list view"""
        return ", ".join([c.name for c in obj.categories.all()])
    display_categories.short_description = 'Categories'

# Register Category admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')

# Register Product admin
admin.site.register(Product, ProductAdmin)
