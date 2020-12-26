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
    NODE_PROPS = ('tag',)

    def prepare_values(self, values):
        values['tag'] = self.eval(self.kwargs.get('tag', 'ul'))

        if self.mode == 'two_line':
            values['class'].append('mdc-list--two-line')


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
    NODE_PROPS = ('tag',)

    def prepare_values(self, values):
        values['tag'] = self.eval(self.kwargs.get('tag', 'li'))


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

    def template_default(self):
        """Get formatted literal string for default List Primary Line.
        """
        return '''
<span class="mdc-list-item__primary-text {class}" {props}>
  {child}
</span>
'''


class LineSecondary(Node):
    """ListItem secondary line.
    """
    WANT_CHILDREN = True

    def template_default(self):
        """Get formatted literal string for default List Secondary Line.
        """
        return '''
<span class="mdc-list-item__secondary-text {class}" {props}>
  {child}
</span>
'''


class Group(Node):
    """ListGroup component.
    """
    WANT_CHILDREN = True
    NODE_PROPS = ('tag',)

    def prepare_values(self, values):
        values['tag'] = self.eval(self.kwargs.get('tag', 'h3'))


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

    def template_default(self):
        """get formatted literal string for default divider.
        """
        return '''
<li role="separator" class="mdc-list-divider {class}" {props}></li>
'''


class SelectList(Node):
    """List component, select variant.
    """
    WANT_CHILDREN = True
    MODES = ('list', 'radio', 'checkbox')
    NODE_PROPS = ('tag',)

    def prepare_values(self, values):
        if self.mode == 'radio':
            values['props'].append(('role', 'radiogroup'))
        elif self.mode == 'checkbox':
            values['props'].append(('role', 'group'))
        else:
            values['props'].append(('role', 'listbox'))
        values['tag'] = self.eval(self.kwargs.get('tag', 'ul'))

        if values['label']:
            values['props'].append(('aria-label', values['label']))

        self.context['item_mode'] = self.mode


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

    def prepare_values(self, values):
        mode = self.context.get('item_mode', 'list')
        selected = self.eval(self.kwargs.get('selected', False))
        input_props = []

        if selected:
            values['props'].append(('tabindex', '0'))

            if mode in ('radio', 'checkbox'):
                values['props'].append(('aria-checked', 'true'))
                input_props.append(('checked', 'checked'))
            else:
                values['props'].append(('aria-selected', 'true'))
                values['class'].append('mdc-list-item--selected')
        else:
            if mode in ('radio', 'checkbox'):
                values['props'].append(('aria-checked', 'false'))
            else:
                values['props'].append(('aria-selected', 'false'))

        values['name'] = self.eval(self.kwargs.get('name'))
        values['value'] = self.eval(self.kwargs.get('value'))

        values['input_props'] = self.join_attributes(input_props)


    @property
    def template(self):
        """Get formatted literal string for Select ListItem.

        Overridden, mode comes from context, from parent Component.
        """
        mode = self.context.get('item_mode', 'list')
        method = getattr(self, 'template_%s' % mode, None)
        if not method:
            raise NotImplementedError("Method is missing: template_%s" % mode)

        return method()


    def template_list(self):
        """Get formatted literal string for list Selection.
        """
        return '''
<li role="option" class="mdc-list-item {class}" {props}>
  {child}
</li>
'''


    def template_radio(self):
        """Get formatted literal string for radio Selection.
        """
        return '''
<li role="radio" class="md-list-item {class}" {props}>
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
</li>
'''


    def template_checkbox(self):
        """Get formatted literal string for checkbox Selection.
        """
        return '''
<li role="checkbox" class="mdc-list-item {class}" {props}>
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
</li>
'''


components = {
    'List': List,
    'List_Item': Item,
    'List_Line_Primary': LinePrimary,
    'List_Line_Secondary': LineSecondary,
    'List_Group': Group,
    'List_Divider': Divider,
    'SelectList': SelectList,
    'SelectList_Item': SelectItem,
}
