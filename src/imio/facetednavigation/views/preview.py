# encoding: utf-8

from Products.Five.browser import BrowserView


class FacetedTableView(BrowserView):

    def render_table(self, batch):
        table = FacetedTable(self.context, self.request)
        table.update(batch)
        return table.render()


from five import grok
from z3c.table import column
from z3c.table.interfaces import IColumn
from z3c.table.table import SequenceTable
from zope.interface import Interface
from zope.interface import implements


class IFacetedTable(Interface):
    pass


class FacetedTable(SequenceTable):
    implements(IFacetedTable)

    cssClasses = {'table': 'listing'}

    cssClassEven = u'odd'
    cssClassOdd = u'even'
    sortOn = 'table-number-0'

    @property
    def values(self):
        return [brain for brain in self.batch]

    def update(self, batch):
        self.batch = batch
        super(FacetedTable, self).update()


class TitleColumn(column.GetAttrColumn, grok.MultiAdapter):
    grok.provides(IColumn)
    grok.name('title_column')
    grok.adapts(Interface, Interface, IFacetedTable)

    header = u'Titre'
    weight = 0

    def renderCell(self, item):
        return '<a href="{0}">{1}</a>'.format(item.getURL(), item.Title)


class AuthorColumn(column.GetAttrColumn, grok.MultiAdapter):
    grok.provides(IColumn)
    grok.name('author_column')
    grok.adapts(Interface, Interface, IFacetedTable)

    header = u'Auteur'
    attrName = 'Creator'
    weight = 10


class StateColumn(column.GetAttrColumn, grok.MultiAdapter):
    grok.provides(IColumn)
    grok.name('state_column')
    grok.adapts(Interface, Interface, IFacetedTable)

    header = u'Etat'
    attrName = 'review_state'
    weight = 20
