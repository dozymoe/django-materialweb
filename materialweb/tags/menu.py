"""
Menu
====

See: https://material.io/components/menus

Menus display a list of choices on temporary surfaces.
"""
from .base import Node
#from .lists import List, Item


class Menu(Node):
    """
    Provides template tag: :code:`Menu`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Menu %}
         {% List %}
           {% List_Item %}
             {% List_Content %}
               {% trans "A Menu Item" %}
             {% endList_Content %}
           {% endList_Item %}

           {% List_Item %}
             {% List_Content %}
               {% trans "Another Menu Item" %}
             {% endList_Content %}
           {% endList_Item %}
         {% endList %}
       {% endMenu %}

    Example output:

    .. code-block:: html

       <div class="mdc-menu mdc-menu-surface">
         <ul class="mdc-list" role="menu" aria-hidden="true"
             aria-orientation="vertical" tabindex="-1">
           <li class="mdc-list-item" role="menuitem">
             <span class="mdc-list-item__ripple"></span>
             <span class="mdc-list-item__text">A Menu Item</span>
           </li>
           <li class="mdc-list-item" role="menuitem">
             <span class="mdc-list-item__ripple"></span>
             <span class="mdc-list-item__text">Another Menu Item</span>
           </li>
         </ul>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def prepare(self):
        self.context['list_props'] = (
            ('role', 'menu'),
            ('aria-hidden', 'true'),
            ('aria-orientation', 'vertical'),
            ('tabindex', '-1'),
        )
        self.context['list_item_props'] = (
            ('role', 'menuitem'),
        )


    def template_default(self):
        return '''
<{tag} class="mdc-menu mdc-menu-surface {class}" {props}>
  {child}
</{tag}>
'''


class Anchor(Node):
    """
    Provides template tag: :code:`Menu_Anchor`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Menu_Anchor id="demo-menu" %}
         {% trans "Open Menu" as label %}
         {% IconButton type="button" label=label class="material-icons" %}
           more_vert
         {% endIconButton %}

         {% Menu %}
         {% endMenu %}
       {% endMenu_Anchor %}

    Example output:

    .. code-block:: html

       <div id="demo-menu" class="mdc-menu-surface--anchor">
         <button type="button" aria-label="Open Menu" title="Open Menu"
             class="mdc-icon-button material-icons">
           more_vert
         </button>

         <div class="mdc-menu mdc-menu-surface">
         </div>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def template_default(self):
        return '''
<{tag} class="mdc-menu-surface--anchor {class}" {props}>
  {child}
</{tag}>
'''


class Group(Node):
    """
    Provides template tag: :code:`Menu_Group`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Menu id="demo-menu" %}
         {% List %}
           {% Menu_Group %}
             {% List_Item %}
               {% List_Image %}...{% endList_Image %}
               {% List_Text %}{% trans "Single" %}{% endList_Text %}
             {% endList_Item %}

             {% List_Item %}
               {% List_Image %}...{% endList_Image %}
               {% List_Text %}1.15{% endList_Text %}
             {% endList_Item %}
           {% endMenu_Group %}

           {% List_Divider %}
           {% List_Item %}
             {% List_Text %}
               {% trans "Add space before paragraph" %}
             {% endList_Text %}
           {% endList_Item %}
         {% endList %}
       {% endMenu %}

    Example output:

    .. code-block:: html

       <div class="mdc-menu mdc-menu-surface" id="demo-menu">
         <ul class="mdc-list" role="menu" aria-hidden="true"
             aria-orientation="vertical" tabindex="-1">
           <li>
             <ul class="mdc-menu__selection-group">
               <li class="mdc-list-item" role="menuitem">
                 <span class="mdc-list-item__ripple"></span>
                 <span class="mdc-list-item__graphic mdc-menu__selection-group-icon">
                   ...
                 </span>
                 <span class="mdc-list-item__text">Single</span>
               </li>
               <li class="mdc-list-item" role="menuitem">
                 <span class="mdc-list-item__ripple"></span>
                 <span class="mdc-list-item__graphic mdc-menu__selection-group-icon">
                  ...
                 </span>
                 <span class="mdc-list-item__text">1.15</span>
               </li>
             </ul>
           </li>
           <li class="mdc-list-divider" role="separator"></li>
           <li class="mdc-list-item" role="menuitem">
             <span class="mdc-list-item__ripple"></span>
             <span class="mdc-list-item__text">Add space before paragraph</span>
           </li>
           ...
         </ul>
       </div>

    """ # pylint:disable=line-too-long

    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'ul'
    "Rendered HTML tag."

    def prepare(self):
        self.context['list_image_class'] = ['mdc-menu__selection-group-icon']


    def template_default(self):
        return '''
<li>
  <{tag} class="mdc-menu__selection-group {class}" {props}>
    {child}
  </{tag}>
</li>
'''


components = {
    'Menu': Menu,
    'Menu_Anchor': Anchor,
    'Menu_Group': Group,
}
