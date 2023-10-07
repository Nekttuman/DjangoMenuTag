from django import template
from menuapp.models import MenuItem
from django.urls import reverse, NoReverseMatch
from django.utils.html import escape, mark_safe

register = template.Library()


# @register.simple_tag
# def draw_menu(menu_name, request):
#     current_url = request.path
#
#     menu_items = MenuItem.objects.filter(menu_name=menu_name)
#
#     def render_menu_item(item):
#         is_active = current_url == item.url
#
#         item_class = "active" if is_active else ""
#
#         try:
#             url = reverse(item.url)
#         except NoReverseMatch:
#             url = item.url
#
#         item_html = f'<li class="{escape(item_class)}"><a href="{escape(url)}">{escape(item.title)}</a></li>'
#
#         return item_html
#
#     menu_html = ""
#     for item in menu_items:
#         menu_html += render_menu_item(item)
#
#     return mark_safe(menu_html)


@register.simple_tag
def draw_menu(menu_name, request):
    current_url = request.path
    print(request.path)
    menu_items = MenuItem.objects.filter(menu_name=menu_name).prefetch_related('children')

    # Find the active item based on the current URL
    active_item = None
    for item in menu_items:
        if current_url == item.url:
            active_item = item
            break

    active_item_parents = []
    if active_item:
        active = active_item
        while active.parent:
            active_item_parents.append(active.parent)
            active = active.parent

    is_expand_prev = True if active_item else False

    def is_item_active(_item):
        return active_item and _item == active_item

    def is_item_parent_active(item):
        return active_item and item in active_item_parents

    def render_menu_item(item):
        is_active = is_item_active(item)
        is_active = is_active or is_item_parent_active(item)

        nonlocal is_expand_prev
        is_expand_prev = False if is_item_active(item) else is_expand_prev

        item_class = "active" if is_active else ""
        item_class += " expand" if is_expand_prev else ""

        item_html = f'<li class="{escape(item_class)}"><a href="{escape(item.url)}">{escape(item.title)}</a>'

        if item.children.exists():
            item_html += '<ul>'
            for child in item.children.all():
                item_html += render_menu_item(child)
            item_html += '</ul>'

        item_html += '</li>'
        return item_html

    menu_html = "<ul>"
    for item in menu_items:
        if not item.parent:
            menu_html += render_menu_item(item)
    menu_html += "</ul>"

    return mark_safe(menu_html)
