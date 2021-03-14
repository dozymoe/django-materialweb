"""
Tabs
====

See: https://material.io/components/tabs

Tabs organize and allow navigation between groups of content that are related
and at the same level of hierarchy.

"""
from .base import Node


class TabBar(Node):
    """
    Provides template tag: :code:`TabBar`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

    .. code-block:: html

       <div class="mdc-tab-bar" role="tablist">
         <div class="mdc-tab-scroller">
           <div class="mdc-tab-scroller__scroll-area">
             <div class="mdc-tab-scroller__scroll-content">
               <button class="mdc-tab mdc-tab--active" role="tab"
                   aria-selected="true" tabindex="0">
                 <span class="mdc-tab__content">
                   <span class="mdc-tab__icon material-icons"
                       aria-hidden="true">
                     favorite
                   </span>
                   <span class="mdc-tab__text-label">Favorites</span>
                 </span>
                 <span class="mdc-tab-indicator mdc-tab-indicator--active">
                   <span class="mdc-tab-indicator__content mdc-tab-indicator__content--underline"></span>
                 </span>
                 <span class="mdc-tab__ripple"></span>
               </button>
             </div>
           </div>
         </div>
       </div>

    """ # pylint:disable=line-too-long

    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('scoll',)
    "Available variants."

    def prepare(self):
        pass

    def template_scroll(self):
        return '''
<{tag} role="tablist" class="mdc-tab-bar {class}" {props}>
  <div class="mdc-tab-scroller">
    <div class="mdc-tab-scroller__scroll-area">
      <div class="mdc-tab-scroller__scroll-content">
      </div>
    </div>
  </div>
</{tag}>
'''


components = {
    'TabBar': TabBar,
}
