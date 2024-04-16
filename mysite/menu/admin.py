from django.contrib import admin

# Register your models here.
from . models import Dish, CartItem

class MenuAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Fundamentals", {
            
            "fields": [
                "name","price"
            ]
        }),
        (
            "Details",
            {"fields":["country_of_origin", "description"]}
        ),
    )
    
admin.site.register(Dish, MenuAdmin)
admin.site.register(CartItem)