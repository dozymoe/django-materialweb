"""
Drawer
======

See: https://material.io/components/navigation-drawer

A navigation drawer provides access to destinations and app functionality, such
as switching accounts. It can either be permanently on-screen or controlled by
a navigation menu icon.

A navigation drawer is recommended for:

 - Apps with five or more top-level destinations
 - Apps with two or more levels of navigation hierarchy
 - Quick navigation between unrelated destinations

"""
from .base import Node


class Drawer(Node):
    """
    Provides template tag: :code:`Drawer`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Drawer %}
         {% Drawer_Content %}
           {% List_Item tag="a" href="#" activate=True aria-current="page" %}
             {% List_Content tag="i" type="image" aria-hidden="true" class="material-icons" %}
               inbox
             {% endList_Content %}
             {% List_Content type="text" %}Inbox{% endList_Content %}
           {% endList_Item %}

           {% List_Item tag="a" href="#" %}
             {% List_Content tag="i" type="image" aria-hidden="true" class="material-icons" %}
               send
             {% endList_Content %}
             {% List_Content type="text" %}Outgoing{% endList_Content %}
           {% endList_Item %}

           {% List_Item tag="a" href="#" %}
             {% List_Content tag="i" type="image" aria-hidden="true" class="material-icons" %}
               drafts
             {% endList_Content %}
             {% List_Content type="text" %}Drafts{% endList_Content %}
           {% endList_Item %}
         {% endDrawer_Content %}
       {% endDrawer %}

    .. code-block:: html

       <aside class="mdc-drawer">
         <div class="mdc-drawer__content">
           <nav class="mdc-list">
             <a href="#" aria-current="page"
                 class="mdc-list-item mdc-list-item--activated">
               <span class="mdc-list-item__ripple"></span>
               <i aria-hidden="true"
                   class="material-icons mdc-list-item__graphic">
                 inbox
               </i>
               <span class="mdc-list-item__text">Inbox</span>
             </a>
             <a class="mdc-list-item" href="#">
               <span class="mdc-list-item__ripple"></span>
               <i aria-hidden="true"
                   class="material-icons mdc-list-item__graphic">
                 send
               </i>
               <span class="mdc-list-item__text">Outgoing</span>
             </a>
             <a class="mdc-list-item" href="#">
               <span class="mdc-list-item__ripple"></span>
               <i aria-hidden="true"
                   class="material-icons mdc-list-item__graphic">
                 drafts
               </i>
               <span class="mdc-list-item__text">Drafts</span>
             </a>
           </nav>
         </div>
       </aside>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('standard', 'modal', 'dismissible')
    "Available variants."
    DEFAULT_TAG = 'aside'
    "Rendered HTML tag."

    def template_standard(self):
        return '''
<{tag} class="mdc-drawer {class}" {props}>
  {child}
</{tag}>
'''


    def template_modal(self):
        return '''
<{tag} class="mdc-drawer mdc-drawer--modal {class}" {props}>
  {child}
</{tag}>
<div class="mdc-drawer-scrim"></div>
'''


    def template_dismissible(self):
        return '''
<{tag} class="mdc-drawer mdc-drawer--dismissible {class}" {props}>
  {child}
</{tag}>
'''


class Header(Node):
    """
    Provides template tag: :code:`Drawer_Header`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Drawer %}
         {% Drawer_Header %}
           {% Drawer_Title %}Mail{% endDrawer_Title %}
           {% Drawer_SubTitle %}email@material.io{% endDrawer_SubTitle %}
         {% endDrawer_Header %}
         {% Drawer_Content %}
           {% List_Item tag="a" href="#" %}
             {% List_Content tag="i" type="image" aria-hidden="true" class="material-icons" %}
               inbox
             {% endList_Content %}
             {% List_Content type="text" %}Inbox{% endList_Content %}
           {% endList_Item %}
         {% endDrawer_Content %}
       {% endDrawer %}

    .. code-block:: html

       <aside class="mdc-drawer">
         <div class="mdc-drawer__header">
           <h3 class="mdc-drawer__title">Mail</h3>
           <h6 class="mdc-drawer__subtitle">email@material.io</h6>
         </div>
         <div class="mdc-drawer__content">
           <nav class="mdc-list">
             <a class="mdc-list-item" href="#">
               <span class="mdc-list-item__ripple"></span>
               <i aria-hidden="true"
                   class="material-icons mdc-list-item__graphic">
                 inbox
               </i>
               <span class="mdc-list-item__text">Inbox</span>
             </a>
           </nav>
         </div>
       </aside>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def template_default(self):
        return '''
<{tag} class="mdc-drawer__header {class}" {props}>
  {child}
</{tag}>
'''


class Title(Node):
    """
    Provides template tag: :code:`Drawer_Title`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Drawer_Header %}
         {% Drawer_Title %}Mail{% endDrawer_Title %}
         {% Drawer_SubTitle %}email@material.io{% endDrawer_SubTitle %}
       {% endDrawer_Header %}

    .. code-block:: html

       <div class="mdc-drawer__header">
         <h3 class="mdc-drawer__title">Mail</h3>
         <h6 class="mdc-drawer__subtitle">email@material.io</h6>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'h3'
    "Rendered HTML tag."

    def template_default(self):
        return '''
<{tag} class="mdc-drawer__title {class}" {props}>
  {child}
</{tag}>
'''


class SubTitle(Node):
    """
    Provides template tag: :code:`Drawer_SubTitle`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Drawer_Header %}
         {% Drawer_Title %}Mail{% endDrawer_Title %}
         {% Drawer_SubTitle %}email@material.io{% endDrawer_SubTitle %}
       {% endDrawer_Header %}

    .. code-block:: html

       <div class="mdc-drawer__header">
         <h3 class="mdc-drawer__title">Mail</h3>
         <h6 class="mdc-drawer__subtitle">email@material.io</h6>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'h6'
    "Rendered HTML tag."

    def template_default(self):
        return '''
<{tag} class="mdc-drawer__subtitle {class}" {props}>
  {child}
</{tag}>
'''


class Content(Node):
    """
    Provides template tag: :code:`Drawer_Content`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% Drawer_Content %}
         {% List_Item tag="a" href="#" %}
           {% List_Content tag="i" type="image" aria-hidden="true" class="material-icons" %}
             inbox
           {% endList_Content %}
           {% List_Content type="text" %}Inbox{% endList_Content %}
         {% endList_Item %}
       {% endDrawer_Content %}

    .. code-block:: html

       <div class="mdc-drawer__content">
         <nav class="mdc-list">
           <a class="mdc-list-item" href="#">
             <span class="mdc-list-item__ripple"></span>
             <i aria-hidden="true"
                 class="material-icons mdc-list-item__graphic">
               inbox
             </i>
             <span class="mdc-list-item__text">Inbox</span>
           </a>
         </nav>
       </div>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'nav'
    "Rendered HTML tag."

    def template_default(self):
        return '''
<div class="mdc-drawer__content">
  <{tag} class="mdc-list {class}" {props}>
    {child}
  </{tag}>
</div>
'''


class AppContent(Node):
    """
    Provides template tag: :code:`Drawer_AppContent`.

    In cases where the drawer occupies the full viewport height, some styles
    must be applied to get the dismissible drawer and the content below the
    top app bar to independently scroll and work in all browsers.

    In the following example, the mdc-drawer__content and main-content elements
    should scroll independently of each other. The mdc-drawer--dismissible and
    mdc-drawer-app-content elements should then sit side-by-side.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       <body>
         {% Drawer mode="dismissible" %}
           {% Drawer_Content %}
             {% List_Item tag="a" href="#" activate=True aria-current="page" %}
               {% List_Content tag="i" type="image" aria-hidden="true" class="material-icons" %}
                 inbox
               {% endList_Content %}
               {% List_Content type="text" %}Inbox{% endList_Content %}
             {% endList_Item %}
  
             {% List_Item tag="a" href="#" %}
               {% List_Content tag="i" type="image" aria-hidden="true" class="material-icons" %}
                 send
               {% endList_Content %}
               {% List_Content type="text" %}Outgoing{% endList_Content %}
             {% endList_Item %}
  
             {% List_Item tag="a" href="#" %}
               {% List_Content tag="i" type="image" aria-hidden="true" class="material-icons" %}
                 drafts
               {% endList_Content %}
               {% List_Content type="text" %}Drafts{% endList_Content %}
             {% endList_Item %}
           {% endDrawer_Content %}
         {% endDrawer %}

         {% Drawer_AppContent %}
           {% TopAppBar %}
             {% TopAppBar_Left %}
               {% TopAppBar_Menu class="material-icons" %}
                 menu
               {% endTopAppBar_Menu %}

               {% TopAppBar_Title %}
                 Dismissible Drawer
               {% endTopAppBar_Title %}
             {% endTopAppBar_Left %}
           {% endTopAppBar %}

           <main id="main-content" class="main-content">
             <div class="mdc-top-app-bar--fixed-adjust">
               App Content
             </div>
           </main>
         {% endDrawer_AppContent %}

       </body>

    .. code-block:: html

       <body>
         <aside class="mdc-drawer mdc-drawer--dismissible">
           <div class="mdc-drawer__content">
             <div class="mdc-list">
               <a href="#" aria-current="page"
                   class="mdc-list-item mdc-list-item--activated">
                 <span class="mdc-list-item__ripple"></span>
                 <i aria-hidden="true"
                     class="material-icons mdc-list-item__graphic">
                   inbox
                 </i>
                 <span class="mdc-list-item__text">Inbox</span>
               </a>
               <a class="mdc-list-item" href="#">
                 <span class="mdc-list-item__ripple"></span>
                 <i aria-hidden="true"
                     class="material-icons mdc-list-item__graphic">
                   send
                 </i>
                 <span class="mdc-list-item__text">Outgoing</span>
               </a>
               <a class="mdc-list-item" href="#">
                 <span class="mdc-list-item__ripple"></span>
                 <i aria-hidden="true"
                     class="material-icons mdc-list-item__graphic">
                   drafts
                 </i>
                 <span class="mdc-list-item__text">Drafts</span>
               </a>
             </div>
           </div>
         </aside>

         <div class="mdc-drawer-app-content">
           <header class="mdc-top-app-bar app-bar" id="app-bar">
             <div class="mdc-top-app-bar__row">
               <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-start">
                 <button class="material-icons mdc-top-app-bar__navigation-icon mdc-icon-button">menu</button>
                 <span class="mdc-top-app-bar__title">Dismissible Drawer</span>
               </section>
             </div>
           </header>

           <main class="main-content" id="main-content">
             <div class="mdc-top-app-bar--fixed-adjust">
               App Content
             </div>
           </main>
         </div>
       </body>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def template_default(self):
        return '''
<{tag} class="mdc-drawer-app-content {class}" {props}>
  {child}
</{tag}>
'''


components = {
    'Drawer': Drawer,
    'Drawer_Header': Header,
    'Drawer_Title': Title,
    'Drawer_SubTitle': SubTitle,
    'Drawer_Content': Content,
    'Drawer_AppContent': AppContent,
}
