from django.contrib import admin
from . models import Dish, CartItem,UserSuggestions

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
admin.site.register(UserSuggestions)