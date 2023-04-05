from django.contrib import admin
from api.models import Post, CustomUser

admin.site.register(CustomUser)
admin.site.register(Post)

# Register your models here.
