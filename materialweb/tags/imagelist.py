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
    MODES = ('default', 'masonry')
    DEFAULT_TAG = 'ul'

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

    WANT_CHILDREN = True
    NODE_PROPS = ('image', 'reversed')
    DEFAULT_TAG = 'li'

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
