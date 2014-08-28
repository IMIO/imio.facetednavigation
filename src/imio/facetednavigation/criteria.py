# encoding: utf-8

from zope.interface import implements

from eea.facetednavigation.criteria.handler import Criteria
from eea.facetednavigation.criteria.interfaces import ICriteria


class CollectionCriteria(Criteria):
    """ Handle criteria """
    implements(ICriteria)
