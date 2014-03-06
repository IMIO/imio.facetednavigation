from zope.interface import implements

from eea.facetednavigation.widgets.storage import Criterion
from eea.facetednavigation.criteria.interfaces import ICriteria

from imio.facetednavigation.widgets.collection.widget import Widget


class CollectionCriteria(object):
    """ Handle criteria
    """
    implements(ICriteria)

    def __init__(self, context):
        pass

    @property
    def criterion(self):
        criterion = Criterion(widget='collection', position=0,
                              section='default')
        return criterion

    def items(self):
        return [('collection', self.criterion)]

    def widget(self, wid=None, cid=None):
        return Widget

    def keys(self):
        return ['collection']

    def values(self):
        return [self.criterion]
