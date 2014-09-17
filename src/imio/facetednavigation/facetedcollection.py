# encoding: utf-8

from Products.Archetypes import atapi
from plone.app.collection.interfaces import ICollection
from plone.app.collection.collection import Collection
from plone.app.collection.collection import CollectionSchema
from imio.facetednavigation import ImioFacetedMessageFactory as _
from zope.interface import implements


class IFacetedCollection(ICollection):
    pass


FacetedCollectionSchema = CollectionSchema.copy() + atapi.Schema((

    atapi.StringField(
        name='category',
        required=False,
        mode='rw',
        vocabulary_factory='imio.facetednavigation.collectioncategoryvocabulary',
        widget=atapi.SelectionWidget(
            label=_(u'category'),
        ),
    ),

))


class FacetedCollection(Collection):
    implements(IFacetedCollection)
    meta_type = 'FacetedCollection'
    schema = FacetedCollectionSchema


atapi.registerType(FacetedCollection, 'imio.facetednavigation')
