from zope.component import getUtility
from zope.interface import implements

from eea.facetednavigation.interfaces import IWidgetsInfo
from eea.facetednavigation.widgets.storage import Criterion
from eea.facetednavigation.criteria.interfaces import ICriteria


class ImioCriteria(object):
    """ Handle criteria """
    implements(ICriteria)

    def __init__(self, context):
        pass

    def get(self, key, default=None):
        """ Get criterion
        """
        for cid, cvalue in self.items():
            if key == cid:
                return cvalue
        return default

    def items(self):
        return [(c.widget, c) for c in self.criterions]

    def widget(self, wid=None, cid=None):
        if not wid:
            criterion = self.get(cid)
            if not criterion:
                raise KeyError(cid)
            wid = criterion.get('widget')
        info = getUtility(IWidgetsInfo)
        return info.widgets.get(wid, None)

    def keys(self):
        return [c.widget for c in self.criterions]

    def values(self):
        return [c for c in self.criterions]


class CollectionCriteria(ImioCriteria):

    @property
    def criterions(self):
        objects = list()
        objects.append(Criterion(widget='collection', position=0,
                                 section='default'))
        objects.append(Criterion(widget='resultsperpage', position=1,
                                 section='default', default=5,
                                 hidden=True))
        return objects
