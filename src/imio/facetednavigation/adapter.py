# encoding: utf-8

from imio.facetednavigation.interfaces import IFacetedCollectionAdvancedFilter
from imio.facetednavigation.interfaces import IWidgetDefaultValue
from five import grok
from zope.interface import Interface


class WidgetValueAdapter(grok.MultiAdapter):
    grok.provides(IWidgetDefaultValue)
    grok.adapts(Interface, Interface, Interface)

    def __init__(self, context, request, widget):
        self.context = context
        self.request = request
        self.widget = widget

    @property
    def value(self):
        return u'ee47847bffbf4c92a2ed0dff531dde75'


class AdvancedFilterAdapter(grok.Adapter):
    grok.provides(IFacetedCollectionAdvancedFilter)
    grok.context(Interface)
    grok.name('advanced-filter')

    def __init__(self, context):
        self.context = context

    @property
    def query(self):
        return {'SearchableText': {'query': u'1'}}
