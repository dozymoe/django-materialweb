"""Implements Material Design Web Componnet: Select

MDC Select provides Material Design single-option select menus, using the MDC
menu. The Select component is fully accessible, and supports RTL rendering.

See: https://material.io/develop/web/components/input-controls/select-menus
"""
import logging
#-
from .base import Node, TextNode

_logger = logging.getLogger(__name__)


class Select(Node):
    """Select component.
    """
    WANT_CHILDREN = True
    WANT_FORM_FIELD = True
    HIDE_FORM_FIELD = True
    MODES = ('filled', 'outlined')
    NODE_PROPS = ('required', 'disabled')
    DEFAULT_TAG = 'ul'

    def prepare_attributes(self, attrs, default):
        """Prepare html input element's attributes.
        """
        if 'required' in self.kwargs and self.eval(self.kwargs['required']):
            attrs['required'] = 'true'

        if 'disabled' in self.kwargs and self.eval(self.kwargs['disabled']):
            attrs['disabled'] = 'true'


    def prepare(self):
        self.values['items'] = '\n'.join(self.render_items())

        field = self.bound_field.field
        choices = {str(choice): text for choice, text in field.choices}
        selected = self.bound_field.value()
        self.values['selected_text'] = choices.get(selected, '')

        anchor_props = []

        if ('required' in self.kwargs and self.eval(self.kwargs['required']))\
                or field.required:
            self.values['class'].append('mdc-select--required')
            anchor_props.append(('aria-required', 'true'))

        if ('disabled' in self.kwargs and self.eval(self.kwargs['disabled']))\
                or field.disabled:
            self.values['class'].append('mdc-select--disabled')
            anchor_props.append(('aria-disabled', 'true'))

        self.values['anchor_props'] = self.join_attributes(anchor_props)


    def render_items(self):
        selected = self.bound_field.value()
        for key, val in self.bound_field.field.choices:
            item = Item(
                    TextNode(val),
                    **{
                        'value': key,
                        'selected': key == selected,
                    })
            yield item.render(self.context)


    def template_filled(self):
        """Get formatted literal string for filled Select.
        """
        return '''
<div class="mdc-select mdc-select--filled {class} {props}">
  {element}
  <div class="mdc-select__anchor" role="button" aria-haspopup="listbox"
      aria-expanded="false" aria-labelledby="{id}-label {id}-selected"
      {anchor_props}>
    <span class="mdc-select__ripple"></span>
    <span id="{id}-label" class="mdc-floating-label">{label}</span>
    <span class="mdc-select__selected-text-container">
      <span id="{id}-selected" class="mdc-select__selected-text">
        {selected_text}
      </span>
    </span>
    <span class="mdc-select__dropdown-icon">
      <svg
          class="mdc-select__dropdown-icon-graphic"
          viewBox="7 10 10 5" focusable="false">
        <polygon
            class="mdc-select__dropdown-icon-inactive"
            stroke="none"
            fill-rule="evenodd"
            points="7 10 12 15 17 10">
        </polygon>
        <polygon
            class="mdc-select__dropdown-icon-active"
            stroke="none"
            fill-rule="evenodd"
            points="7 15 12 10 17 15">
        </polygon>
      </svg>
    </span>
    <span class="mdc-line-ripple"></span>
  </div>

  <div class="mdc-select__menu mdc-menu mdc-menu-surface mdc-menu-surface--fullwidth">
    <{tag} class="mdc-list" role="listbox" aria-label="{label}">
      {child}
      {items}
    </{tag}>
  </div>
</div>
'''


    def template_outlined(self):
        """Get formatted literal string for filled Select.
        """
        return '''
<div class="mdc-select mdc-select--outlined {class} {props}">
  {element}
  <div class="mdc-select__anchor" role="button" aria-haspopup="listbox"
      aria-expanded="false" aria-labelledby="{id}-label {id}-selected"
      {anchor_props}>
    <span class="mdc-notched-outline">
      <span class="mdc-notched-outline__leading"></span>
      <span class="mdc-notched-outline__notch">
        <span id="{id}-label" class="mdc-floating-label">
          {label}
        </span>
      </span>
      <span class="mdc-notched-outline__trailing"></span>
    </span>
    <span class="mdc-select__selected-text-container">
      <span id="{id}-selected" class="mdc-select__selected-text">
        {selected_text}
      </span>
    </span>
    <span class="mdc-select__dropdown-icon">
      <svg
          class="mdc-select__dropdown-icon-graphic"
          viewBox="7 10 10 5" focusable="false">
        <polygon
            class="mdc-select__dropdown-icon-inactive"
            stroke="none"
            fill-rule="evenodd"
            points="7 10 12 15 17 10">
        </polygon>
        <polygon
            class="mdc-select__dropdown-icon-active"
            stroke="none"
            fill-rule="evenodd"
            points="7 15 12 10 17 15">
        </polygon>
      </svg>
    </span>
    <span class="mdc-line-ripple"></span>
  </div>

  <div class="mdc-select__menu mdc-menu mdc-menu-surface mdc-menu-surface--fullwidth">
    <{tag} class="mdc-list" role="listbox" aria-label="{label}">
      {child}
      {items}
    </{tag}>
  </div>
</div>
'''


class Item(Node):
    """Select list item.
    """
    WANT_CHILDREN = True
    NODE_PROPS = ('value', 'selected', 'disabled')
    DEFAULT_TAG = 'li'

    def prepare(self):
        self.values['value'] = self.eval(self.kwargs['value'])
        if self.eval(self.kwargs.get('selected', False)):
            self.values['selected'] = 'true'
            self.values['class'].append('mdc-list-item--selected')
        else:
            self.values['selected'] = 'false'

        if self.eval(self.kwargs.get('disabled', False)):
            self.values['class'].append('mdc-list-item--disabled')
            self.values['props'].append(('aria-disabled', 'true'))


    def template_default(self):
        return '''
<{tag} class="mdc-list-item {class}" aria-selected="{selected}"
    data-value="{value}" role="option" {props}>
  <span class="mdc-list-item__ripple"></span>
  <span class="mdc-list-item__text">{child}</span>
</{tag}>
'''


components = {
    'Select': Select,
    'Select_Item': Item,
}
