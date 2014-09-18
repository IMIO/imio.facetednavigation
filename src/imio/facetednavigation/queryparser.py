# encoding: utf-8

from imio.facetednavigation.interfaces import IFacetedCollectionAdvancedFilter
from zope.component import queryAdapter


def _filter_is(context, row):
    named_adapter = queryAdapter(context, IFacetedCollectionAdvancedFilter,
                                 name=row.values)
    if named_adapter:
        return named_adapter.query
    return {}
