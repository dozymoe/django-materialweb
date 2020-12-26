"""Implements Material Design Web Component: ImageList

MDC Image List provides a RTL-aware Material Design image list component.
An Image List consists of several items, each containing an image and
optionally supporting content (i.e. a text label).

See: https://material-components.github.io/material-components-web-catalog/#/component/image-list
""" # pylint:disable=line-too-long

from .base import Node


class ImageList(Node):
    """Imagelist component.
    """

    WANT_CHILDREN = True

    NODE_PROPS = ('mode', 'class')

    def prepare_values(self, values):
        if self.mode == 'masonry':
            values['class'].append('mdc-image-list--masonry')

        # Send this to ListItem
        self.context['mode'] = self.mode


    @property
    def template(self):
        return '''
<ul class="mdc-image-list {class}" {props}>
  {child}
</ul>
'''


class ListItem(Node):

    WANT_CHILDREN = True
    MODES = ('default', 'masonry')

    NODE_PROPS = ('image', 'reversed', 'class')

    @property
    def template(self):
        image = self.kwargs.get('image', None)
        reverse = 'reversed' in self.args or self.kwargs.get('reversed', False)

        # Coming from ImageList
        mode = self.context.get('mode', None)

        if image:
            if mode == 'masonry':
                part1 = self.template_image_masonry()
            else:
                part1 = self.template_image_normal()
        else:
            part1 = ''

        part2 = '''
  <div class="mdc-image-list__supporting">
    <div class="mdc-image-list__label">
      {child}
    </div>
  </div>
'''

        template = ['<li class="mdc-image-list__item {class}">']

        if reverse:
            template.append(part2)
            template.append(part1)
        else:
            template.append(part1)
            template.append(part2)

        template.append('</li>')

        return ''.join(template)


    def template_image_normal(self):
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
