from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from menu_app.models import Menu


class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(Menu, MenuItemMPTTModelAdmin)
