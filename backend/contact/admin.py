from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "phone_number",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
    )
    list_filter = (
        "first_name",
        "last_name",
        "email",
    )


admin.site.register(Contact, ContactAdmin)
