from django.contrib import admin

from myapp1.models import TelegramUsers, Roles

# Register your models here.

admin.site.register(TelegramUsers)
admin.site.register(Roles)