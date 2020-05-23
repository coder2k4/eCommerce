from django.contrib import admin
from products.models import Product
from tags.models import Tag


# todo: сделать вид как у горизонтального фильтра?
class TagInline(admin.TabularInline):
    model = Tag.products.through
    raw_id_fields = ("tag",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    prepopulated_fields = {"slug": ("title",)}

    inlines = [
        TagInline,
    ]

    filter_horizontal = ["tags"]

    save_as = True
    save_on_top = True

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
