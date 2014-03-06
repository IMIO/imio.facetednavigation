from eea.facetednavigation.widgets.widget import Widget as AbstractWidget


def empty(*args, **kwargs):
    return ''


class Widget(AbstractWidget):

    widget_type = 'collection'
    widget_label = 'Collection'
    index = empty

    def query(self, form):
        """ Get value from form and return a catalog dict query
        """
        query = {'SearchableText': 'Plone'}
        return query
