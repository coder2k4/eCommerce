from django.contrib import admin

# Register your models here.
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    prepopulated_fields = {"slug": ("title",)}

    save_as = True
    save_on_top = True

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
