# encoding: utf-8

from Products.Five.browser import BrowserView


class FacetedTableView(BrowserView):

    def render_table(self, batch):
        table = FacetedTable(self.context, self.request)
        table.update(batch)
        return table.render()


from ZTUtils import make_query
from five import grok
from z3c.table import column
from z3c.table.header import SortingColumnHeader
from z3c.table.interfaces import IColumn
from z3c.table.interfaces import IColumnHeader
from z3c.table.table import SequenceTable
from zope.interface import Interface
from zope.interface import implements
from zope.publisher.interfaces.browser import IBrowserRequest


class IFacetedTable(Interface):
    pass


class FacetedTable(SequenceTable):
    implements(IFacetedTable)

    cssClasses = {'table': 'listing'}

    cssClassEven = u'odd'
    cssClassOdd = u'even'
    sortOn = 'table-number-0'

    def sortRows(self):
        self.sortOn = self.update_sortOn()
        super(FacetedTable, self).sortRows()

    def update_sortOn(self):
        sort_on = self.request.form.get('c0[]', '')
        for c in self.columns:
            key = c.sort_index or c.attrName
            if key == sort_on:
                return c.id
        return self.columns[0].id

    def getSortOrder(self):
        reverse = self.request.form.get('reversed[]', '')
        if reverse == 'on':
            return u'descending'
        return u'ascending'

    @property
    def values(self):
        return [brain for brain in self.batch]

    def update(self, batch):
        self.batch = batch
        super(FacetedTable, self).update()


class BaseColumn(column.GetAttrColumn):

    sort_index = None

    def getSortKey(self, item):
        attr = self.sort_index or self.attrName
        if attr is None:
            raise ValueError('sort_index or attrName must be defined')
        return getattr(item, attr)

    def renderCell(self, item):
        return getattr(item, self.attrName.decode('utf8'))


class BaseColumnHeader(SortingColumnHeader, grok.MultiAdapter):
    grok.adapts(Interface, IBrowserRequest, IFacetedTable, IColumn)
    grok.provides(IColumnHeader)

    def render(self):
        if self.column.sort_index or self.column.attrName:
            html = u'<a href="{0}#{1}" title="Sort">{2} {3}</a>'
            return html.format(self.faceted_url, self.query_string,
                               self.column.header, self.order_arrow)
        return self.column.header

    @property
    def sort_on(self):
        return self.column.sort_index or self.column.attrName

    @property
    def faceted_url(self):
        return '/'.join(self.request.get('URL').split('/')[:-1])

    @property
    def query_string(self):
        query = self.request_query

        if (query.get('c0', '') == self.sort_on or
            self.table.sortOn == self.column.id) and \
           query.get('reversed', 'off') == 'off':
            query.update({'reversed': 'on'})
        elif 'reversed' in query:
            del query['reversed']
        query.update({'c0': self.sort_on})
        if 'version' in query:
            del query['version']
        return make_query(query)

    @property
    def request_query(self):
        query = dict(self.request.form)
        return {k.replace('[]', ''): v for k, v in query.items()}

    @property
    def order_arrow(self):
        query = self.request_query
        if query.get('c0', '') == self.sort_on or \
           self.table.sortOn == self.column.id:
            order = query.get('reversed')
            if order == 'on':
                return u'v'
            else:
                return u'^'
        return u''


class TitleColumn(BaseColumn, grok.MultiAdapter):
    grok.provides(IColumn)
    grok.name('title_column')
    grok.adapts(Interface, Interface, IFacetedTable)

    header = u'Titre'
    weight = 0
    sort_index = 'sortable_title'

    def getSortKey(self, item):
        from Products.CMFPlone.CatalogTool import sortable_title
        return sortable_title(item)()

    def renderCell(self, item):
        return u'<a href="{0}">{1}</a>'.format(item.getURL(),
                                               item.Title.decode('utf8'))


class AuthorColumn(BaseColumn, grok.MultiAdapter):
    grok.provides(IColumn)
    grok.name('author_column')
    grok.adapts(Interface, Interface, IFacetedTable)

    header = u'Auteur'
    attrName = 'Creator'
    weight = 10


class StateColumn(BaseColumn, grok.MultiAdapter):
    grok.provides(IColumn)
    grok.name('state_column')
    grok.adapts(Interface, Interface, IFacetedTable)

    header = u'Etat'
    attrName = 'review_state'
    weight = 20
