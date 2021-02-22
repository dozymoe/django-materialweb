"""
Button
======

See: https://material.io/components/buttons

Buttons allow users to take actions, and make choices, with a single tap.

"""
from .base import Node


class Button(Node):
    """
    Provides template tag: :code:`Button`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Button mode="raised" type="submit" %}
         {% Button_Label %}
           {% trans "Submit" %}
         {% endButton_Label %}
       {% endButton %}

       {% url 'login' as url %}
       {% Button mode="outlined" tag="a" href=url %}
         {% Button_Label %}
           {% trans "Log In" %}
         {% endButton_Label %}
       {% endButton %}

    Example output:

    .. code-block:: html

       <div class="mdc-touch-target-wrapper">
         <button type="submit" class="mdc-button mdc-button--raised">
           <span class="mdc-button__ripple"></span>
           <span class="mdc-button__label">Submit</span>
         </button>
       </div>

       <div class="mdc-touch-target-wrapper">
         <a href="/login" class="mdc-button mdc-button--outlined">
           <span class="mdc-button__ripple"></span>
           <span class="mdc-button__label">Log In</span>
         </a>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('outlined', 'raised')
    "Available variants."
    DEFAULT_TAG = 'button'
    "Rendered HTML tag."

    def prepare(self):
        if 'button_class' in self.context:
            self.values['class'].extend(self.context['button_class'])

        if self.mode == 'outlined':
            self.values['class'].append('mdc-button--outlined')
        elif self.mode == 'raised':
            self.values['class'].append('mdc-button--raised')


    @property
    def template(self):
        return '''
<div class="mdc-touch-target-wrapper">
  <{tag} class="mdc-button mdc-button--touch {class}" {props}>
    <span class="mdc-button__ripple"></span>
    {child}
    <span class="mdc-button__touch"></span>
  </{tag}>
</div>
'''


class Label(Node):
    """
    Provides template tag: :code:`Banner_Label`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Button_Label id="mylabel" %}
         {% trans "My Accessible Button" %}
       {% endButton_Label %}

    Example output:

    .. code-block:: html

       <span id="mylabel" class="mdc-button__label">My Accessible Button</span>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'span'
    "Rendered HTML tag."

    def template_default(self):
        return '''
<{tag} class="mdc-button__label {class}" {props}>
  {child}
</{tag}>
'''


class Icon(Node):
    """
    Provides template tag: :code:`Button_Icon`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Button_Icon %}
         <i class="fa fa-circle"></i>
       {% endButton_Icon %}

    Example output:

    .. code-block:: html

       <span aria-hidden="true" class="mdc-button__icon">
         <i class="fa fa-circle"></i>
       </span>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'span'
    "Rendered HTML tag."

    def prepare(self):
        if 'button_icon_class' in self.context:
            self.values['class'].extend(self.context['button_icon_class'])


    def template_default(self):
        return '''
<{tag} aria-hidden="true" class="mdc-button__icon {class}" {props}>
  {child}
</{tag}>
'''


class IconButton(Node):
    """
    Provides template tag: :code:`IconButton`.

    See: https://material.io/develop/web/components/buttons/icon-buttons

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% trans "Save" as label %}
       {% IconButton label=label type="button" class="material-icons" %}
         save
       {% endIconButton %}

    .. code-block:: html

       <button aria-label="Save" title="Save" type="button"
           class="mdc-icon-button material-icons">
         save
       </button>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'button'
    "Rendered HTML tag."

    def prepare(self):
        if 'button_icon_class' in self.context:
            self.values['class'].extend(self.context['button_icon_class'])
        elif 'button_class' in self.context:
            self.values['class'].extend(self.context['button_class'])


    def template_default(self):
        return '''
<{tag} aria-label="{label}" title="{label}" {props}
    class="mdc-icon-button {class}">
  {child}
</{tag}>
'''


class ToggleButton(Node):
    """
    Provides template tag: :code:`ToggleButton`.

    See: https://material.io/develop/web/components/buttons/icon-buttons

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% trans "Add to favorites" as label %}
       {% ToggleButton state=False icon_when_on="favorite" icon_when_off="favorite_border" label=label id="add-to-favorites" %}

    Example output:

    .. code-block:: html

       <button id="add-to-favorites" class="mdc-icon-button"
           aria-label="Add to favorites" aria-pressed="false">
         <i class="material-icons mdc-icon-button__icon mdc-icon-button__icon--on">
           favorite
         </i>
         <i class="material-icons mdc-icon-button__icon">
           favorite_border
         </i>
       </button>

    """ # pylint:disable=line-too-long
    NODE_PROPS = ('type', 'state', 'icon_when_on', 'icon_when_off')
    "Extended Template Tag arguments."

    def prepare(self):
        self.values['state'] = self.eval(self.kwargs.get('state'))
        self.values['icon_when_on'] = self.kwargs['icon_when_on']
        self.values['icon_when_off'] = self.kwargs['icon_when_off']

        if 'button_class' in self.context:
            self.values['class'].extend(self.context['button_class'])

        if self.values['state']:
            self.values['class'].append('mdc-icon-button--on')
            self.values['props'].append(('aria-pressed', 'true'))


    def template_default(self):
        return '''
<button type="button" aria-label="{label}" title="{label}" {props}
    class="mdc-icon-button toggle {class}">
  <i class="material-icons mdc-icon-button__icon mdc-icon-button__icon--on">
    {icon_when_on}
  </i>
  <i class="material-icons mdc-icon-button__icon">
    {icon_when_off}
  </i>
</button>
'''


components = {
    'Button': Button,
    'Button_Icon': Icon,
    'Button_Label': Label,
    'IconButton': IconButton,
    'ToggleButton': ToggleButton,
}
