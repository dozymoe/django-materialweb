import logging
from yarl import URL
#-
from django.utils.translation import gettext as _
#-
from .base import Node, TextNode
from .button import IconButton, Icon

_logger = logging.getLogger(__name__)


class DataTable(Node):

    WANT_CHILDREN = True
    NODE_PROPS = ('name', 'pager', 'page_name', 'row_selectable', 'row_movable')
    DEFAULT_TAG = 'table'

    def prepare(self):
        self.context['name'] = self.eval(self.kwargs.get('name', ''))
        self.context['selectable'] = self.eval(
                self.kwargs.get('row_selectable'))
        self.context['movable'] = self.eval(
                self.kwargs.get('row_movable'))

        pager = self.eval(self.kwargs.get('pager'))
        if pager:
            self.values['pagination'] = self.render_pagination(pager)
        else:
            self.values['pagination'] = ''


    def render_pagination(self, pager):
        url = URL(self.context['request'].get_full_path())
        page_name = self.eval(self.kwargs.get('page_name', 'page'))

        if pager.has_previous():
            first_kwargs = {'href': url % {page_name: 1}}
            next_kwargs = {'href': url % {page_name: pager.next_page_number()}}
            extra_kwargs = {}
        else:
            first_kwargs = next_kwargs = {}
            extra_kwargs = {'type': 'button', 'disabled': 'disabled'}

        first_button = IconButton(
                Icon(TextNode('first_page')),
                **{
                    'label': _("First Page"),
                    'data-first-page': 'true',
                    'class': 'material-icons mdc-data-table__pagination-button',
                },
                **first_kwargs,
                **extra_kwargs)
        prev_button = IconButton(
                Icon(TextNode('chevron_left')),
                **{
                    'label': _("Previous Page"),
                    'data-prev-page': 'true',
                    'class': 'material-icons i'
                        'mdc-data-table__pagination-button',
                },
                **next_kwargs,
                **extra_kwargs)

        if pager.has_next():
            first_kwargs = {'href': url % {page_name: 1}}
            next_kwargs = {'href': url % {page_name: pager.next_page_number()}}
            extra_kwargs = {}
        else:
            next_kwargs = last_kwargs = {}
            extra_kwargs = {'type': 'button', 'disabled': 'disabled'}

        next_button = IconButton(
                Icon(TextNode('chevron_right')),
                **{
                    'label': _("Next Page"),
                    'data-next-page': 'true',
                    'class': 'material-icons mdc-data-table__pagination-button',
                },
                **next_kwargs,
                **extra_kwargs)
        last_button = IconButton(
                Icon(TextNode('last_page')),
                **{
                    'label': _("Last Page"),
                    'data-last-page': 'true',
                    'class': 'material-icons mdc-data-table__pagination-button',
                },
                **last_kwargs,
                **extra_kwargs)

        values = {
            'page_size': pager.paginator.per_page,
            'total_pages': pager.paginator.num_pages,
            'total_items': pager.paginator.count,
            'start': pager.start_index(),
            'end': pager.end_index(),
            'first_button': first_button.render(self.context),
            'prev_button': prev_button.render(self.context),
            'next_button': next_button.render(self.context),
            'last_button': last_button.render(self.context),
            'label_rows_per_page': _("Rows per page"),
            'id_page_size': self.id + '-pagesize',
        }
        template = '''
<div class="mdc-data-table__pagination">
  <div class="mdc-data-table__pagination-trailing">
    <div class="mdc-data-table__pagination-rows-per-page">
      <div class="mdc-data-table__pagination-rows-per-page-label">
        {label_rows_per_page}
      </div>

      <div class="mdc-select mdc-select--outlined mdc-select--no-label mdc-data-table__pagination-rows-per-page-select">
        <div role="button" aria-haspopup="listbox"
            aria-labelledby="{id_page_size}" tabindex="0"
            class="mdc-select__anchor">
          <span id="{id_page_size}" class="mdc-select__selected-text">
            {page_size}
          </span>
          <span class="mdc-select__dropdown-icon">
            <svg
                class="mdc-select__dropdown-icon-graphic"
                viewBox="7 10 10 5">
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
          <span class="mdc-notched-outline mdc-notched-outline--notched">
            <span class="mdc-notched-outline__leading"></span>
            <span class="mdc-notched-outline__trailing"></span>
          </span>
        </div>

        <div role="listbox"
            class="mdc-select__menu mdc-menu mdc-menu-surface mdc-menu-surface--fullwidth">
          <ul class="mdc-list">
            <li aria-selected="true" role="option" data-value="10"
                class="mdc-list-item mdc-list-item--selected">
              <span class="mdc-list-item__text">10</span>
            </li>
            <li class="mdc-list-item" role="option" data-value="25">
              <span class="mdc-list-item__text">25</span>
            </li>
            <li class="mdc-list-item" role="option" data-value="100">
              <span class="mdc-list-item__text">100</span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div class="mdc-data-table__pagination-navigation">
      <div class="mdc-data-table__pagination-total">
        {start}‑{end} of {total_items}
      </div>
      {first_button}
      {prev_button}
      {next_button}
      {last_button}
    </div>
  </div>
</div>
'''
        return template.format(**values)


    def template_default(self):
        return '''
<div class="mdc-data-table">
  <div class="mdc-data-table__table-container">
    <{tag} aria-label="{label}" {props} class="mdc-data-table__table {class}">
      {child}
    </{tag}>
  </div>
  {pagination}
</div>
'''


class Head(Node):

    WANT_CHILDREN = True
    DEFAULT_TAG = 'thead'

    def template_default(self):
        return '<{tag} {props} class="{class}">{child}</{tag}>'


class HeadRow(Node):

    WANT_CHILDREN = True
    DEFAULT_TAG = 'tr'

    def prepare(self):
        if self.context['selectable']:
            self.values['select_checkbox'] = self.render_select()
        else:
            self.values['select_checkbox'] = ''

        self.values['label_toggle_all'] = _("Toggle all rows")


    def render_select(self):
        return '''
<th role="columnheader" scope="col"
    class="mdc-data-table__header-cell mdc-data-table__header-cell--checkbox">
  <div class="mdc-checkbox mdc-data-table__header-row-checkbox mdc-checkbox--selected">
    <input type="checkbox" aria-label="{label_toggle_all}"
        class="mdc-checkbox__native-control" />
    <div class="mdc-checkbox__background">
      <svg viewBox="0 0 24 24" class="mdc-checkbox__checkmark">
        <path fill="none" d="M1.73,12.91 8.1,19.28 22.79,4.59"
            class="mdc-checkbox__checkmark-path" />
      </svg>
      <div class="mdc-checkbox__mixedmark"></div>
    </div>
    <div class="mdc-checkbox__ripple"></div>
  </div>
</th>
'''


    def template_default(self):
        return '''
<{tag} {props} class="mdc-data-table__header-row {class}">
  {select_checkbox}
  {child}
</{tag}>
'''


class HeadColumn(Node):

    WANT_CHILDREN = True
    NODE_PROPS = ('type',)
    DEFAULT_TAG = 'th'

    def prepare(self):
        type_ = self.kwargs.get('type')
        if type_ == 'num':
            self.values['class'].append('mdc-data-table__header-cell--numeric')


    def template_default(self):
        return '''
<{tag} role="columnheader" scope="col" {props}
    class="mdc-data-table__header-cell {class}">
  {child}
</{tag}>
'''


class Body(Node):

    WANT_CHILDREN = True
    DEFAULT_TAG = 'tbody'

    def template_default(self):
        return '''
<{tag} {props} class="mdc-data-table__content {class}">
  {child}
</{tag}>
'''


class BodyRow(Node):

    WANT_CHILDREN = True
    NODE_PROPS = ('value',)
    DEFAULT_TAG = 'tr'

    def prepare(self):
        if self.context['selectable']:
            self.context['id_row_header'] = self.id + '-header'
            self.values['select_checkbox'] = self.render_select()
        else:
            self.values['select_checkbox'] = ''


    def render_select(self):
        values = {
            'name': self.context.get('name', ''),
            'value': self.eval(self.kwargs.get('value', '')),
            'id_row_header': self.context['id_row_header'],
        }
        template = '''
<td class="mdc-data-table__cell mdc-data-table__cell--checkbox">
  <div class="mdc-checkbox mdc-data-table__row-checkbox">
    <input name="{name}" value="{value}" type="checkbox"
        aria-labelledby="{id_row_header}"
        class="mdc-checkbox__native-control" />
    <div class="mdc-checkbox__background">
      <svg viewBox="0 0 24 24" class="mdc-checkbox__checkmark">
        <path fill="none" d="M1.73,12.91 8.1,19.28 22.79,4.59"
            class="mdc-checkbox__checkmark-path" />
      </svg>
      <div class="mdc-checkbox__mixedmark"></div>
    </div>
    <div class="mdc-checkbox__ripple"></div>
  </div>
</td>
'''
        return template.format(**values)


    def template_default(self):
        return '''
<{tag} {props} class="mdc-data-table__row {class}">
  {select_checkbox}
  {child}
</{tag}>
'''


class BodyColumn(Node):

    WANT_CHILDREN = True
    NODE_PROPS = ('type',)
    DEFAULT_TAG = 'td'

    def prepare(self):
        type_ = self.kwargs.get('type')
        if type_ == 'num':
            self.values['class'].append('mdc-data-table__header-cell--numeric')


    def template_default(self):
        return '''
<{tag} {props} class="mdc-data-table__cell {class}">
  {child}
</{tag}>
'''


class BodyColumnHeader(Node):

    WANT_CHILDREN = True
    NODE_PROPS = ('type',)
    DEFAULT_TAG = 'th'

    def prepare(self):
        type_ = self.kwargs.get('type')
        if type_ == 'num':
            self.values['class'].append('mdc-data-table__header-cell--numeric')

        if 'id_row_header' in self.context:
            self.values['props'].append(('id', self.context['id_row_header']))


    def template_default(self):
        return '''
<{tag} scope="row" {props} class="mdc-data-table__cell {class}">
  {child}
</{tag}>
'''


components = {
    'DataTable': DataTable,
    'DataTable_Head': Head,
    'DataTable_Head_Row': HeadRow,
    'DataTable_Head_Col': HeadColumn,
    'DataTable_Body': Body,
    'DataTable_Row': BodyRow,
    'DataTable_Col': BodyColumn,
    'DataTable_ColHeader': BodyColumnHeader,
}
