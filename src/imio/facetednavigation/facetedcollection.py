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
        name='talcondition',
        required=False,
        mode='rw',
        widget=atapi.StringWidget(
            label=_(u'TAL condition'),
            description=_(u'TAL expression for the display of the collection'),
        ),
    ),

    atapi.StringField(
        name='collectioncategory',
        required=False,
        mode='rw',
        vocabulary_factory='imio.facetednavigation.facetedcollectioncategoryvocabulary',
        widget=atapi.SelectionWidget(
            label=_(u'Category'),
            description=u'',
            format='select',
        ),
    ),

))


class FacetedCollection(Collection):
    implements(IFacetedCollection)
    meta_type = 'FacetedCollection'
    schema = FacetedCollectionSchema


atapi.registerType(FacetedCollection, 'imio.facetednavigation')
