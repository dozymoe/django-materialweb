"""
Card
====

See: https://material.io/components/cards

Cards contain content and actions about a single subject.

"""
from .base import Node


class Card(Node):
    """
    Provides template tag: :code:`Card`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Card %}
         {% Card_PrimaryAction %}
           {% Card_Media class="mdc-card__media--square" %}
             Title
           {% endCard_Media %}
           <!-- ... additional primary action content ... -->
         {% endCard_PrimaryAction %}

         {% Card_Actions %}
           <div class="mdc-card__action-buttons">
             {% Button %}
               {% Button_Label %}Action 1{% endButton_Label %}
             {% endButon %}
             {% Button %}
               {% Button_Label %}Action 2{% endButton_Label %}
             {% endButon %}
           </div>
           <div class="mdc-card__action-icons">

             {% trans "Share" as label %}
             {% IconButton label=label class="material-icons" %}
               share
             {% endIconButton %}

             {% trans "More options" as label %}
             {% IconButton label=label class="material-icons" %}
               more_vert
             {% endIconButton %}
           </div>
         {% endCard_Actions %}
       {% endCard %}

    Example output:

    .. code-block:: html

       <div class="mdc-card">
         <div class="mdc-card__primary-action">
           <div class="mdc-card__media mdc-card__media--square">
             <div class="mdc-card__media-content">Title</div>
           </div>
           <!-- ... additional primary action content ... -->
         </div>
         <div class="mdc-card__actions">
           <div class="mdc-card__action-buttons">
             <button class="mdc-button mdc-card__action mdc-card__action--button">
               <div class="mdc-button__ripple"></div>
               <span class="mdc-button__label">Action 1</span>
             </button>
             <button class="mdc-button mdc-card__action mdc-card__action--button">
               <div class="mdc-button__ripple"></div>
               <span class="mdc-button__label">Action 2</span>
             </button>
           </div>
           <div class="mdc-card__action-icons">
             <button class="material-icons mdc-icon-button mdc-card__action mdc-card__action--icon" title="Share">share</button>
             <button class="material-icons mdc-icon-button mdc-card__action mdc-card__action--icon" title="More options">more_vert</button>
           </div>
         </div>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('elevated', 'outlined')
    "Available variants."

    def prepare(self):
        if self.mode == 'elevated':
            self.values['class'].append('mdc-card--elevated')
        elif self.mode == 'outlined':
            self.values['class'].append('mdc-card--outlined')


    @property
    def template(self):
        return '''
<{tag} class="mdc-card {class}" {props}>
  {child}
</{tag}>
'''


class PrimaryAction(Node):
    """
    Provides template tag: :node:`Card_PrimaryAction`.

    If a majority of the card (or even the entire card) should be actionable.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Card_PrimaryAction tabindex="0" %}
         <!-- content within actionable area -->
       {% endCard_PrimaryAction %}

    Example output:

    .. code-block:: html

       <div class="mdc-card__primary-action" tabindex="0">
         <!-- content within actionable area -->
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def template_default(self):
        return '''
<{tag} class="mdc-card__primary-action {class}" tabindex="0" {props}>
  {child}
</{tag}>
'''


class RichMedia(Node):
    """
    Provides template tag: :code:`Card_Media`.

    This area is used for showing rich media in cards, and optionally as a
    container.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Card_Media class="my-card__media mdc-card__media--16-9" %}
         Title
       {% endCard_Media %}

    Example output:

    .. code-block:: html

       <div class="my-card__media mdc-card__media mdc-card__media--16-9">
         <div class="mdc-card__media-content">Title</div>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('default', 'square')
    "Available variants."

    def prepare(self):
        if self.mode == 'square':
            self.values['class'].append('mdc-card__media--square')


    @property
    def template(self):
        return '''
<{tag} class="mdc-card__media {class}" {props}>
  <div class="mdc-card__media-content">
    {child}
  </div>
</{tag}>
'''


class Actions(Node):
    """
    Provides template tag: :code:`Card_Actions`.

    This area is used to show different actions the user can take, typically at
    the bottom of a card. It's often used with buttons.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Card_Actions mode="full_bleed" %}
         {% Button tag="a" href="#" %}
           {% Button_Label %}
             {% trans "All Business Headlines" %}
           {% endButton_Label %}
           {% Button_Icon tag="i" class="material-icons" %}
             arrow_forward
           {% endButton_Icon %}
         {% endButton %}
       {% endCard_Actions %}

    Example output:

    .. code-block:: html

       <div class="mdc-card__actions mdc-card__actions--full-bleed">
         <a class="mdc-button mdc-card__action mdc-card__action--button" href="#">
           <div class="mdc-button__ripple"></div>
           <span class="mdc-button__label">All Business Headlines</span>
           <i class="material-icons mdc-button__icon" aria-hidden="true">arrow_forward</i>
         </a>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('default', 'full_bleed')
    "Available variants."

    def prepare(self):
        if self.mode == 'full_bleed':
            self.values['class'].append('mdc-card__actions--full-bleed')

        self.context['button_class'] = ['mdc-card__action',
                'mdc-card__action--button']
        self.context['button_icon_class'] = ['mdc-card__action',
                'mdc-card__action--icon']


    @property
    def template(self):
        return '''
<{tag} class="mdc-card__actions {class}" {props}>
  {child}
</{tag}>
'''


class Content(Node):
    """
    Provides template tag: :code:`Card_Content`.

    It can occasionally be useful to add non-semantic elements to a card. For
    instance, some implementations might do this to add an overlay layer.

    In this case, it's important to delineate between semantic (real) content
    and non-semantic content added by the implementation. To achieve this,
    simply wrap the semantic content in an mdc-card__content element. The
    non-semantic content can remain at the card's top level.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Card %}
         {% Card_Content %}
           <!-- ... semantic content ... -->
         {% endCard_Content %}
         <!-- ... non-semantic content ... -->
       {% endCard %}


    Example output:

    .. code-block:: html

       <div class="mdc-card">
         <div class="mdc-card__content">
           <!-- ... semantic content ... -->
         </div>
         <!-- ... non-semantic content ... -->
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def template_default(self):
        return '''
<{tag} class="mdc-card__content {class}" {props}>
  {child}
</{tag}>
'''


components = {
    'Card': Card,
    'Card_PrimaryAction': PrimaryAction,
    'Card_Media': RichMedia,
    'Card_Actions': Actions,
    'Card_Content': Content,
}
