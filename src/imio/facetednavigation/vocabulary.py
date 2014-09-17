# encoding: utf-8

from Products.CMFPlone.utils import safe_unicode
from plone import api
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


def safe_encode(term):
    if isinstance(term, unicode):
        # no need to use portal encoding for transitional encoding from
        # unicode to ascii. utf-8 should be fine.
        term = term.encode('utf-8')
    return term


class FacetedCollectionVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context, query=None):
        self.context = context

        results = [(b.Title, b.UID) for b in self.brains]
        items = [
            SimpleTerm(uid, uid, safe_unicode(title))
            for title, uid in results
            if query is None or safe_encode(query) in safe_encode(title)
        ]
        sorted(items)

        return SimpleVocabulary(items)

    @property
    def brains(self):
        catalog = api.portal.get_tool('portal_catalog')
        return catalog({'portal_type': 'FacetedCollection'})


FacetedCollectionVocabularyFactory = FacetedCollectionVocabulary()


class FacetedCollectionCategoryVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context, query=None):
        items = [
            SimpleTerm('category1', 'category1', 'Category 1'),
            SimpleTerm('category2', 'category2', 'Category 2'),
        ]
        return SimpleVocabulary(items)


FacetedCollectionCategoryVocabularyFactory = FacetedCollectionCategoryVocabulary()
