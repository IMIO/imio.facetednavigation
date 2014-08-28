# encoding: utf-8

from Products.CMFPlone.utils import safe_unicode
from binascii import b2a_qp
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


class TestVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context, query=None):
        self.context = context
        elements = ('Plone', 'Doc', 'Bienvenue')
        items = [
            SimpleTerm(e, b2a_qp(safe_encode(e)), safe_unicode(e))
            for e in elements
            if query is None or safe_encode(query) in safe_encode(e)
        ]

        return SimpleVocabulary(items)


TestVocabularyFactory = TestVocabulary()


class TestSecondVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context, query=None):
        self.context = context
        elements = ('Plone', '1')
        items = [
            SimpleTerm(e, b2a_qp(safe_encode(e)), safe_unicode(e))
            for e in elements
            if query is None or safe_encode(query) in safe_encode(e)
        ]

        return SimpleVocabulary(items)


TestSecondVocabularyFactory = TestSecondVocabulary()
