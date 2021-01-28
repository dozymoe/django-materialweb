from .base import Node


class Snackbar(Node):

    WANT_CHILDREN = True
    NODE_PROPS = ('stacked', 'leading')

    def prepare(self):
        stacked = self.eval(self.kwargs.get('stacked'))
        if stacked:
            self.values['class'].append('mdc-snackbar--stacked')
        leading = self.eval(self.kwargs.get('leading'))
        if leading:
            self.values['class'].append('mdc-snackbar--leading')


    def template_default(self):
        """Get formatted literal string for Snackbar.
        """
        return '''
<div class="mdc-snackbar {class}" {props}>
  <{tag} role="status" aria-relevant="additions" class="mdc-snackbar__surface">
    {child}
  </{tag}>
</div>
'''


class Label(Node):

    WANT_CHILDREN = True

    def template_default(self):
        """Get formatted literal string for Snackbar Label.
        """
        return '''
<{tag} aria-atomic="false" class="mdc-snackbar__label {class}" {props}>
  {child}
</{tag}>
'''


class Actions(Node):

    WANT_CHILDREN = True

    def prepare(self):
        self.context['button_class'] = ['mdc-snackbar__action']


    def template_default(self):
        """Get formatted literal string for Snackbar Actions.
        """
        return '''
<{tag} aria-atomic="true" class="mdc-snackbar__actions {class}" {props}>
  {child}
</{tag}>
'''


components = {
    'Snackbar': Snackbar,
    'Snackbar_Content': Label,
    'Snackbar_Actions': Actions,
}
