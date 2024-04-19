from django.contrib import admin
from home.views import ChefDetails, BlogDetails,BookATable, Table, Review
# Register your models here.
admin.site.register(ChefDetails)
admin.site.register(BlogDetails)
admin.site.register(BookATable)
admin.site.register(Table)
admin.site.register(Review)
