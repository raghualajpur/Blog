from feed.models import post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(post,PostAdmin)
