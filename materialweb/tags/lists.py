"""Implements Material Design Web Component: List

Lists are continuous, vertical indexes of text or images.

See: https://material.io/components/lists
"""
from .base import Node

class List(Node):
    """List component.
    """
    WANT_CHILDREN = True
    MODES = ('one_line', 'two_line')
    DEFAULT_TAG = 'ul'

    def prepare(self):
        if self.mode == 'two_line':
            self.values['class'].append('mdc-list--two-line')


    @property
    def template(self):
        """Get formatted literal string for default List.

        Overridden because they are the same.
        """
        return '''
<{tag} class="mdc-list {class}" {props}>
  {child}
</{tag}>
'''


class Item(Node):
    """ListItem component.
    """
    WANT_CHILDREN = True
    DEFAULT_TAG = 'li'

    def template_default(self):
        """Get formatted literal string for default ListItem.
        """
        return '''
<{tag} class="mdc-list-item {class}" {props}>
  <span class="mdc-list-item__ripple"></span>
  <span class="mdc-list-item__text">{child}</span>
</{tag}>
'''


class LinePrimary(Node):
    """ListItem primary line.
    """
    WANT_CHILDREN = True
    DEFAULT_TAG = 'span'

    def template_default(self):
        """Get formatted literal string for default List Primary Line.
        """
        return '''
<{tag} class="mdc-list-item__primary-text {class}" {props}>
  {child}
</{tag}>
'''


class LineSecondary(Node):
    """ListItem secondary line.
    """
    WANT_CHILDREN = True
    DEFAULT_TAG = 'span'

    def template_default(self):
        """Get formatted literal string for default List Secondary Line.
        """
        return '''
<{tag} class="mdc-list-item__secondary-text {class}" {props}>
  {child}
</{tag}>
'''


class Group(Node):
    """ListGroup component.
    """
    WANT_CHILDREN = True
    DEFAULT_TAG = 'h3'

    def template_default(self):
        """Get formatted literal string for default List Group.
        """
        return '''
<div class="mdc-list-group {class}" {props}>
  <{tag} class="mdc-list-group__subheader">{label}</{tag}>
  {child}
</div>
'''


class Divider(Node):
    """List divider.
    """
    DEFAULT_TAG = 'li'

    def template_default(self):
        """get formatted literal string for default divider.
        """
        return '''
<{tag} role="separator" class="mdc-list-divider {class}" {props}></{tag}>
'''


class SelectList(Node):
    """List component, select variant.
    """
    WANT_CHILDREN = True
    MODES = ('list', 'radio', 'checkbox')
    DEFAULT_TAG = 'ul'

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


    @property
    def template(self):
        """Get formatted literal string for selection List.

        Overridden because the template are the same.
        """
        return '''
<{tag} class="mdc-list {class}" {props}>
  {child}
</{tag}>
'''


class SelectItem(Node):
    """Select List item.
    """
    WANT_CHILDREN = True
    NODE_PROPS = ('selected', 'name', 'value')
    DEFAULT_TAG = 'li'

    def prepare(self):
        # Late declaration of `self.mode`.
        self.mode = self.context.get('list_mode', 'list')

        selected = self.eval(self.kwargs.get('selected', False))
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
        """Get formatted literal string for list Selection.
        """
        return '''
<{tag} role="option" class="mdc-list-item {class}" {props}>
  {child}
</{tag}>
'''


    def template_radio(self):
        """Get formatted literal string for radio Selection.
        """
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
  <label class="mdc-list-item__text" for="{id}">{label}</label>
</{tag}>
'''


    def template_checkbox(self):
        """Get formatted literal string for checkbox Selection.
        """
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
  <label class="mdc-list-item__text" for="{id}">{label}</label>
</{tag}>
'''


components = {
    'List': List,
    'List_Item': Item,
    'List_LinePrimary': LinePrimary,
    'List_LineSecondary': LineSecondary,
    'List_Group': Group,
    'List_Divider': Divider,
    'SelectList': SelectList,
    'SelectList_Item': SelectItem,
}
