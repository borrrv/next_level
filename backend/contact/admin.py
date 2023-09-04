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

    def save_model(self, request, obj, form, change):
        obj.set_password(obj.password)
        obj.save()


admin.site.register(Contact, ContactAdmin)
