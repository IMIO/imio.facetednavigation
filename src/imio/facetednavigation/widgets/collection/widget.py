# encoding: utf-8

from Products.CMFCore.utils import getToolByName
from eea.facetednavigation.widgets.radio.widget import Widget as RadioWidget
from plone.app.querystring import queryparser
from imio.facetednavigation.interfaces import IWidgetDefaultValue
from zope.component import queryMultiAdapter


class Widget(RadioWidget):

    widget_type = 'collection'
    widget_label = 'Collection'

    def query(self, form):
        """ Get value from form and return a catalog dict query """
        # we receive the UID of the selected Collection
        # get the collection, compute the query and return it
        collection_uid = form.get(self.data.__name__, '')
        if collection_uid:
            # get the collection and compute the query
            catalog = getToolByName(self.context, 'portal_catalog')
            brains = catalog(UID=collection_uid)
            collection = brains[0].getObject()
            return queryparser.parseFormquery(self.context, collection.query)
        return {}

    def count(self, brains, sequence=None):
        """
        """
        res = {}
        if not sequence:
            sequence = [key for key, value in self.vocabulary()]

        ctool = getToolByName(self.context, 'portal_catalog')
        for value in sequence:
            if not value:
                res[value] = len(brains)
                continue
            res[value] = len(ctool(self.query(form={self.data.__name__: value})))
        return res

    @property
    def default(self):
        """Return the default value"""
        default = super(Widget, self).default
        if not default:
            default = self.adapter_default_value
        if not default and self.hidealloption is True:
            default = self.default_term_value
        return default

    @property
    def adapter_default_value(self):
        adapter = queryMultiAdapter((self.context, self.request, self),
                                    IWidgetDefaultValue)
        if adapter:
            return adapter.value

    @property
    def default_term_value(self):
        idx = self.sortreversed and -1 or 0
        terms = self.portal_vocabulary()
        if len(terms) > 0:
            return terms[idx][0]

    @property
    def sortreversed(self):
        return bool(int(getattr(self.data, 'sortreversed', u'0') or u'0'))

    @property
    def hidealloption(self):
        return bool(int(getattr(self.data, 'hidealloption', u'0') or u'0'))
