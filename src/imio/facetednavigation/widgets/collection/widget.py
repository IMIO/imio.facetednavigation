# encoding: utf-8

from eea.facetednavigation.widgets.radio.widget import Widget as RadioWidget
from plone.app.querystring import queryparser
from Products.CMFCore.utils import getToolByName


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
