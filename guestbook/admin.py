from django.contrib import admin
from guestbook.models import Guestbook

# Register your models here.


class GuestbookAdmin(admin.ModelAdmin):
    list_display = ["posted", "user", "content"]
    list_filter = ["posted"]
    list_display_links = ["user", "posted"]
    search_fields = ["user"]
    date_hierarchy = "posted"
    preserve_filters = False
    list_editable = ["content"]
    actions_on_bottom = True
    actions_on_top = False


admin.site.register(Guestbook, GuestbookAdmin)