"""
Banner
======

See: https://material.io/components/banners

A banner displays an important, succinct message, and provides actions for
users to address (or dismiss the banner). It requires a user action to be
dismissed.

Banners should be displayed at the top of the screen, below a top app bar.
They’re persistent and nonmodal, allowing the user to either ignore them or
interact with them at any time. Only one banner should be shown at a time.

"""
from .base import Node


class Banner(Node):
    """
    Provides template tag: :code:`Banner`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Banner %}
         {% Banner_Content %}
           {% Banner_Text %}
             {% trans "There was a problem processing a transaction on your credit card." %}
           {% endBanner_Text %}
         {% endBanner_Content %}
         {% Banner_Actions %}
           {% Button type="button" class="mdc-banner__primary-action" %}
             {% Button_Label %}
               {% trans "Fix it" %}
             {% endButton_Label %}
           {% endButton %}
         {% endBanner_Actions %}
       {% endBanner %}

    Example output:

    .. code-block:: html

       <div class="mdc-banner" role="banner">
         <div class="mdc-banner__content" role="status" aria-live="assertive">
           <div class="mdc-banner__graphic-text-wrapper">
             <div class="mdc-banner__text">
               There was a problem processing a transaction on your credit card.
             </div>
           </div>
           <div class="mdc-banner__actions">
             <button type="button" class="mdc-button mdc-banner__primary-action">
               <span class="mdc-button__ripple"></span>
               <span class="mdc-button__label">Fix it</span>
             </button>
           </div>
         </div>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('default', 'stacked')
    "Available variants."

    def prepare(self):
        if self.mode == 'stacked':
            self.values['class'].append('mdc-banner--mobile-stacked')


    @property
    def template(self):
        return '''
<{tag} class="mdc-banner {class}" role="banner" {props}>
  <div class="mdc-banner__content" role="status" aria-live="assertive">
    {child}
  </div>
</{tag}>
'''


class Content(Node):
    """
    Provides template tag: :code:`Banner_Content`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Banner_Content %}
         {% Banner_Icon class="material-icons" %}
           error_outline
         {% endBanner_Icon %}
         {% Banner_Text %}
           {% trans "There was a problem processing a transaction on your credit card." %}
         {% endBanner_Text %}
       {% endBanner_Content %}

    Example output:

    .. code-block:: html

       <div class="mdc-banner__graphic-text-wrapper">
         <div class="mdc-banner__graphic" role="img" alt="">
           <i class="material-icons mdc-banner__icon">error_outline</i>
         </div>
         <div class="mdc-banner__text">
           There was a problem processing a transaction on your credit card.
         </div>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def template_default(self):
        return '''
<{tag} class="mdc-banner__graphic-text-wrapper {class}" {props}>
  {child}
</{tag}>
'''


class Icon(Node):
    """
    Provides template tag: :code:`Banner_Icon`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% trans "Back" as label %}
       {% Banner_Icon label=label class="material-icons" %}
         arrow_back
       {% endBanner_Icon %}

    Example output:

    .. code-block:: html

       <div class="mdc-banner__graphic" role="img" alt="Back" title="Back">
         <span class="mdc-banner__icon material-icons">
           arrow_back
         </span>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def template_default(self):
        return '''
<{tag} class="mdc-banner__graphic" role="img" alt="{label}" title="{label}">
  <span class="mdc-banner__icon {class}" {props}>
    {child}
  </span>
</{tag}>
'''


class Text(Node):
    """
    Provides template tag: :code:`Banner_Text`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Banner_Text %}
         {% trans "Message that needs immediate action." %}
       {% endBanner_Text %}

    Example output:

    .. code-block:: html

       <div class="mdc-banner__text">
         Message that needs immediate action.
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def template_default(self):
        return '''
<{tag} class="mdc-banner__text {class}" {props}>
  {child}
</{tag}>
'''


class Actions(Node):
    """
    Provides template tag: :code:`Banner_Actions`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Banner_Actions %}
         {% Button type="button" id="btnFixIt" class="mdc-banner__primary-action" %}
           {% Button_Label %}
             {% trans "Fix it" %}
           {% endButton_Label %}
         {% endButton %}
       {% endBanner_Actions %}

    Example output:

    .. code-block:: html

       <div class="mdc-banner__actions">
         <button type="button" class="mdc-button mdc-banner__primary-action">
           <span class="mdc-button__ripple"></span>
           <span class="mdc-button__label">Fix it</span>
         </button>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def template_default(self):
        return '''
<{tag} class="mdc-banner__actions {class}" {props}>
  {child}
</{tag}>
'''


components = {
    'Banner': Banner,
    'Banner_Content': Content,
    'Banner_Icon': Icon,
    'Banner_Text': Text,
    'Banner_Actions': Actions,
}
