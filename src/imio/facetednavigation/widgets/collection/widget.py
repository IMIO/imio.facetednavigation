# encoding: utf-8

from eea.facetednavigation.widgets.radio.widget import Widget as RadioWidget


class Widget(RadioWidget):

    widget_type = 'collection'
    widget_label = 'Collection'

    def query(self, form):
        """ Get value from form and return a catalog dict query """
        searchable_text = form.get(self.data.__name__, '')
        if searchable_text:
            return {'UID': searchable_text}
        return {}
