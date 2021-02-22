"""
List
====

See: https://material.io/components/lists

Lists are continuous, vertical indexes of text or images.
"""
from .base import Node


class List(Node):
    """
    Provides template tag: :code:`List`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% List %}
         {% List_Item tabindex="0" %}
           {% List_Content %}
             {% trans "Single-line item" %}
           {% endList_Content %}
         {% endList_Item %}

         {% List_Item %}
           {% List_Content %}
             {% trans "Single-line item" %}
           {% endList_Content %}
         {% endList_Item %}
       {% endList %}

    Example output:

    .. code-block:: html

       <ul class="mdc-list">
         <li class="mdc-list-item" tabindex="0">
           <span class="mdc-list-item__ripple"></span>
           <span class="mdc-list-item__text">Single-line item</span>
         </li>
         <li class="mdc-list-item">
           <span class="mdc-list-item__ripple"></span>
           <span class="mdc-list-item__text">Single-line item</span>
         </li>
       </ul>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('one_line', 'two_line')
    "Available variants."
    DEFAULT_TAG = 'ul'
    "Rendered HTML tag."

    def prepare(self):
        if self.mode == 'two_line':
            self.values['class'].append('mdc-list--two-line')


    @property
    def template(self):
        return '''
<{tag} class="mdc-list {class}" {props}>
  {child}
</{tag}>
'''


class Item(Node):
    """
    Provides template tag: :code:`List_Item`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% List mode="two_line" %}
         {% List_Item tabindex="0" %}
           {% List_Content %}
             {% List_LinePrimary %}
               {% trans "Two-line item" %}
             {% endList_LinePrimary %}

             {% List_LineSecondary %}
               {% trans "Secondary text" %}
             {% endList_LineSecondary %}
           {% endList_Content %}
         {% endList_Item %}

         {% List_Item %}
           {% List_Content %}
             {% List_LinePrimary %}
               {% trans "Two-line item" %}
             {% endList_LinePrimary %}

             {% List_LineSecondary %}
               {% trans "Secondary text" %}
             {% endList_LineSecondary %}
           {% endList_Content %}
         {% endList_Item %}
       {% endList %}

    Example output:

    .. code-block:: html

       <ul class="mdc-list mdc-list--two-line">
         <li class="mdc-list-item" tabindex="0">
           <span class="mdc-list-item__ripple"></span>
           <span class="mdc-list-item__text">
             <span class="mdc-list-item__primary-text">Two-line item</span>
             <span class="mdc-list-item__secondary-text">Secondary text</span>
           </span>
         </li>
         <li class="mdc-list-item">
           <span class="mdc-list-item__ripple"></span>
           <span class="mdc-list-item__text">
             <span class="mdc-list-item__primary-text">Two-line item</span>
             <span class="mdc-list-item__secondary-text">Secondary text</span>
           </span>
         </li>
       </ul>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('activated',)
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'li'
    "Rendered HTML tag."

    def prepare(self):
        activated = self.eval(self.kwargs.get('activated'))
        if activated:
            self.values['class'].append('mdc-list-item--activated')


    def template_default(self):
        """Get formatted literal string for default ListItem.
        """
        return '''
<{tag} class="mdc-list-item {class}" {props}>
  <span class="mdc-list-item__ripple"></span>
  {child}
</{tag}>
'''


class Content(Node):
    """
    Provides template tag: :code:`List_Content`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% List_Content type="text" %}
         {% trans "line item" %}
       {% endList_Content %}

    Example output:

    .. code-block:: html

       <span class="mdc-list-item__text">line item</span>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('type',)
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'span'
    "Rendered HTML tag."

    def prepare(self):
        type_ = self.eval(self.kwargs.get('type', 'text'))
        if (type_ == 'image'):
            self.values['class'].append('mdc-list-item__graphic')
        else:
            self.values['class'].append('mdc-list-item__text')


    def template_default(self):
        return '<{tag} class="{class}" {props}>{child}</{tag}>'


class LinePrimary(Node):
    """
    Provides template tag: :code:`List_LinePrimary`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% List_LinePrimary %}
         {% trans "Two-line item" %}
       {% endList_LinePrimary %}

    Example output:

    .. code-block:: html

       <span class="mdc-list-item__primary-text">Two-line item</span>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'span'
    "Rendered HTML tag."

    def template_default(self):
        return '''
<{tag} class="mdc-list-item__primary-text {class}" {props}>
  {child}
</{tag}>
'''


class LineSecondary(Node):
    """
    Provides template tag: :code:`List_LineSecondary`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% List_LineSecondary %}
         {% trans "Secondary text" %}
       {% endList_LineSecondary %}

    Example output:

    .. code-block:: html

       <span class="mdc-list-item__secondary-text">Secondary text</span>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'span'
    "Rendered HTML tag."

    def template_default(self):
        return '''
<{tag} class="mdc-list-item__secondary-text {class}" {props}>
  {child}
</{tag}>
'''


class Group(Node):
    """
    Provides template tag: :code:`List_Group`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% List_Group %}
         {% List_Header %}{% trans "List 1" %}{% endList_Header %}
         {% List %}
           {% List_Item tabindex="0" %}
             {% List_Content %}{% trans "line item %}{% endList_Content %}
           {% endList_Item %}

           {% List_Item %}
             {% List_Content %}{% trans "line item %}{% endList_Content %}
           {% endList_Item %}

           {% List_Item %}
             {% List_Content %}{% trans "line item %}{% endList_Content %}
           {% endList_Item %}
         {% endList %}
       {% endList_Group %}

    Example output:

    .. code-block:: html

       <div class="mdc-list-group">
         <h3 class="mdc-list-group__subheader">List 1</h3>
         <ul class="mdc-list">
           <li class="mdc-list-item" tabindex="0">
             <span class="mdc-list-item__ripple"></span>
             <span class="mdc-list-item__text">line item</span>
           </li>
           <li class="mdc-list-item">
             <span class="mdc-list-item__ripple"></span>
             <span class="mdc-list-item__text">line item</span>
           </li>
           <li class="mdc-list-item">
             <span class="mdc-list-item__ripple"></span>
             <span class="mdc-list-item__text">line item</span>
           </li>
         </ul>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def template_default(self):
        return '''
<{tag} class="mdc-list-group {class}" {props}>
  {child}
</{tag}>
'''


class GroupHeader(Node):
    """
    Provides template tag: :code:`List_Header`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% List_Group %}
         {% List_Header %}
           {% trans "List 1" %}
         {% endList_Header %}
       {% endList_Group %}

    Example output:

    .. code-block:: html

       <div class="mdc-list-group">
         <h3 class="mdc-list-group__subheader">List 1</h3>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'h3'
    "Rendered HTML tag."

    def template_default(self):
        return '''
<{tag} class="mdc-list-group__subheader {class}" {props}>
  {child}
</{tag}>
'''


class Divider(Node):
    """
    Provides template tag: :code:`List_Divider`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% List_Divider %}

    Example output:

    .. code-block:: html

       <li role="separator" class="mdc-list-divider"></li>

    """
    DEFAULT_TAG = 'li'
    "Rendered HTML tag."

    def template_default(self):
        return '''
<{tag} role="separator" class="mdc-list-divider {class}" {props}></{tag}>
'''


class SelectList(Node):
    """
    Provides template tag: :code:`SelectList`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% SelectList mode="radio" value="2" %}
         {% SelectList_Item name="demo-list-radio-item-group" value="1" %}
           {% trans "Option 1" %}
         {% endSelectList_Item %}

         {% SelectList_Item name="demo-list-radio-item-group" value="2" %}
           {% trans "Option 2" %}
         {% endSelectList_Item %}
       {% endSelectList %}

    Example output:

    .. code-block:: html

       <ul class="mdc-list" role="radiogroup">
         <li class="mdc-list-item" role="radio" aria-checked="false">
           <span class="mdc-list-item__ripple"></span>
           <span class="mdc-list-item__graphic">
             <div class="mdc-radio">
               <input class="mdc-radio__native-control"
                     type="radio"
                     id="demo-list-radio-item-1"
                     name="demo-list-radio-item-group"
                     value="1">
               <div class="mdc-radio__background">
                 <div class="mdc-radio__outer-circle"></div>
                 <div class="mdc-radio__inner-circle"></div>
               </div>
             </div>
           </span>
           <label for="demo-list-radio-item-1" class="mdc-list-item__text">
             Option 1
           </label>
         </li>
         <li role="radio" aria-checked="true" tabindex="0"
             class="mdc-list-item">
           <span class="mdc-list-item__ripple"></span>
           <span class="mdc-list-item__graphic">
             <div class="mdc-radio">
               <input class="mdc-radio__native-control"
                     type="radio"
                     id="demo-list-radio-item-2"
                     name="demo-list-radio-item-group"
                     value="2"
                     checked>
               <div class="mdc-radio__background">
                 <div class="mdc-radio__outer-circle"></div>
                 <div class="mdc-radio__inner-circle"></div>
               </div>
             </div>
           </span>
           <label for="demo-list-radio-item-2" class="mdc-list-item__text">
             Option 2
           </label>
         </li>
         <li class="mdc-list-item" role="radio" aria-checked="false">
           <span class="mdc-list-item__ripple"></span>
           <span class="mdc-list-item__graphic">
             <div class="mdc-radio">
               <input class="mdc-radio__native-control"
                     type="radio"
                     id="demo-list-radio-item-3"
                     name="demo-list-radio-item-group"
                     value="3">
               <div class="mdc-radio__background">
                 <div class="mdc-radio__outer-circle"></div>
                 <div class="mdc-radio__inner-circle"></div>
               </div>
             </div>
           </span>
           <label for="demo-list-radio-item-3" class="mdc-list-item__text">
             Option 3
           </label>
         </li>
       </ul>

    """ # pylint:disable=line-too-long
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('list', 'radio', 'checkbox')
    "Available variants."
    NODE_PROPS = ('value',)
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'ul'
    "Rendered HTML tag."

    def prepare(self):
        if self.mode == 'radio':
            self.values['props'].append(('role', 'radiogroup'))
        elif self.mode == 'checkbox':
            self.values['props'].append(('role', 'group'))
        else:
            self.values['props'].append(('role', 'listbox'))

        if self.values['label']:
            self.values['props'].append(('aria-label', self.values['label']))

        self.context['list_mode'] = self.mode
        self.context['list_value'] = self.eval(self.kwargs.get('value', ''))


    @property
    def template(self):
        return '''
<{tag} class="mdc-list {class}" {props}>
  {child}
</{tag}>
'''


class SelectItem(Node):
    """Select List item.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('name', 'value')
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'li'
    "Rendered HTML tag."

    def prepare(self):
        # Late declaration of `self.mode`.
        self.mode = self.context.get('list_mode', 'list')
        selected = self.context.get('list_value', '')

        input_props = []

        if selected:
            self.values['props'].append(('tabindex', '0'))

            if self.mode in ('radio', 'checkbox'):
                self.values['props'].append(('aria-checked', 'true'))
                input_props.append(('checked', 'checked'))
            else:
                self.values['props'].append(('aria-selected', 'true'))
                self.values['class'].append('mdc-list-item--selected')
        else:
            if self.mode in ('radio', 'checkbox'):
                self.values['props'].append(('aria-checked', 'false'))
            else:
                self.values['props'].append(('aria-selected', 'false'))

        self.values['name'] = self.eval(self.kwargs.get('name'))
        self.values['value'] = self.eval(self.kwargs.get('value'))

        self.values['input_props'] = self.join_attributes(input_props)


    def template_list(self):
        return '''
<{tag} role="option" class="mdc-list-item {class}" {props}>
  {child}
</{tag}>
'''


    def template_radio(self):
        return '''
<{tag} role="radio" class="md-list-item {class}" {props}>
  <span class="mdc-list-item__ripple"></span>
  <span class="mdc-list-item__graphic">
    <div class="mdc-radio">
      <input name="{name}" value="{value}" type="radio"
          id="{id}" class="mdc-radio__native-control" {input_props}>
      <div class="mdc-radio__background">
        <div class="mdc-radio__outer-circle"></div>
        <div class="mdc-radio__inner-circle"></div>
      </div>
    </div>
  </span>
  <label class="mdc-list-item__text" for="{id}">{child}</label>
</{tag}>
'''


    def template_checkbox(self):
        return '''
<{tag} role="checkbox" class="mdc-list-item {class}" {props}>
  <span class="mdc-list-item__ripple"></span>
  <span class="mdc-list-item__graphic">
    <div class="mdc-checkbox">
      <input name="{name}" value="{value}" type="checkbox"
          id="{id}" class="mdc-checkbox__native-control" {input_props}>
      <div class="mdc-checkbox__background">
        <svg class="mdc-checkbox__checkmark" viewBox="0 0 24 24">
          <path class="mdc-checkbox__checkmark-path" fill="none"
              d="M1.73,12.91 8.1,19.28 22.79,4.59"/>
        </svg>
        <div class="mdc-checkbox__mixedmark"></div>
      </div>
    </div>
  </span>
  <label class="mdc-list-item__text" for="{id}">{child}</label>
</{tag}>
'''


components = {
    'List': List,
    'List_Item': Item,
    'List_Content': Content,
    'List_LinePrimary': LinePrimary,
    'List_LineSecondary': LineSecondary,
    'List_Group': Group,
    'List_Header': GroupHeader,
    'List_Divider': Divider,
    'SelectList': SelectList,
    'SelectList_Item': SelectItem,
}
