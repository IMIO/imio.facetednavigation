# encoding: utf-8

from eea.facetednavigation.subtypes.interfaces import IFacetedNavigable
from zope.interface import Interface


class ICollectionFacetApplied(IFacetedNavigable):
    pass


class IFacetedTable(Interface):
    pass


class IWidgetDefaultValue(Interface):
    pass


class IFacetedCollectionAdvancedFilter(Interface):
    pass


class IFacetedCollectionCategories(Interface):
    pass
