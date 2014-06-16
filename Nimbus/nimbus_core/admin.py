from django.contrib import admin
from .models import Media



class MediaAdmin(admin.ModelAdmin):
    fields = ("id",
              "name",
              "target_url",
              "target_file",
              "user")
    list_display = ("id",
                    "url_hash",
                    "name",
                    "user",
                    "target_url",
                    "target_file",
                    "upload_date",
                    "view_count",
                    "media_category")
    list_filter = ("media_category",)
    search_fields = ("id",
                     "url_hash",
                     "name",
                     "user__username",
                     "target_url",
                     "target_file",
                     "upload_date",
                     "view_count",
                     "media_category")

admin.site.register(Media, MediaAdmin)
