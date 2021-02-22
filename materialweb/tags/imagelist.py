"""
ImageList
=========

See: https://material.io/components/image-lists

Image lists display a collection of images in an organized grid.

"""
from .base import Node


class ImageList(Node):
    """
    Provides template tag: :code:`ImageList`.

    .. code-block:: jinja

       {% load materialweb %}

       {% ImageList mode="masonry" class="my-masonry-image-list" %}
         {% ImageList_Item image="..." %}
           {% trans "Text Label" %}
         {% endImageList_Item %}
       {% endImageList %}

    Example output:

    .. code-block:: html

       <ul class="mdc-image-list mdc-image-list--masonry my-masonry-image-list">
         <li class="mdc-image-list__item">
           <img class="mdc-image-list__image" src="...">
           <div class="mdc-image-list__supporting">
             <span class="mdc-image-list__label">Text label</span>
           </div>
         </li>
       </ul>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('default', 'masonry')
    "Available variants."
    DEFAULT_TAG = 'ul'
    "Rendered HTML tag."

    def prepare(self):
        if self.mode == 'masonry':
            self.values['class'].append('mdc-image-list--masonry')

        # Send this to ListItem
        self.context['list_mode'] = self.mode


    @property
    def template(self):
        return '''
<{tag} class="mdc-image-list {class}" {props}>
  {child}
</{tag}>
'''


class ListItem(Node):
    """
    Provides template tag: :code:`ImageList_Item`.

    Example usage:

    .. code-block:: jinja

       {% load materialweb %}

       {% ImageList_Item image="..." %}
         {% trans "Text Label %}
       {% endImageList_Item %}

    Example output:

    .. code-block:: html

       <li class="mdc-image-list__item">
         <div class="mdc-image-list__image-aspect-container">
           <img class="mdc-image-list__image" src="...">
         </div>
         <div class="mdc-image-list__supporting">
           <span class="mdc-image-list__label">Text label</span>
         </div>
       </li>

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('image', 'reversed')
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'li'
    "Rendered HTML tag."

    @property
    def template(self):
        image = self.eval(self.kwargs.get('image'))
        reverse = 'reversed' in self.args or\
                self.eval(self.kwargs.get('reversed'))

        # Coming from ImageList
        mode = self.context.get('list_mode')

        if image:
            if mode == 'masonry':
                part1 = self.template_image_masonry()
            else:
                part1 = self.template_image_default()
        else:
            part1 = ''

        part2 = '''
  <div class="mdc-image-list__supporting">
    <div class="mdc-image-list__label">
      {child}
    </div>
  </div>
'''

        template = ['<{tag} class="mdc-image-list__item {class}">']

        if reverse:
            template.append(part2)
            template.append(part1)
        else:
            template.append(part1)
            template.append(part2)

        template.append('</{tag}>')

        return ''.join(template)


    def template_image_default(self):
        return '''
  <div class="mdc-image-list__image-aspect-container">
    <img class="mdc-image-list__image" src="{image}" {props}>
  </div>
'''


    def template_image_masonry(self):
        return '''
  <img class="mdc-image-list__image" src="{image}" {props}>
'''


components = {
    'ImageList': ImageList,
    'ImageList_Item': ListItem,
}
