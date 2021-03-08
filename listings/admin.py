from django.contrib import admin
from .models import Listing


# Register your models here.
# fields we want to show in admin, what to click, what to filter etc.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'title',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state','price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
