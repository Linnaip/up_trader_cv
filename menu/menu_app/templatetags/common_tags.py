from django import template
from menu_app.models import Menu
register = template.Library()


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def show_menu(context):
    menu_items = Menu.objects.filter(level=1)
    return {
        "menu_items": menu_items,
    }
