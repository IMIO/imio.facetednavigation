# -*- extra stuff goes here -*-
from zope.i18nmessageid.message import MessageFactory

ImioFacetedMessageFactory = MessageFactory('imiofaceted')


def initialize(context):
    from Products.Archetypes import atapi
    from Products.CMFCore import utils

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes('imio.facetednavigation'),
        'imio.facetednavigation')

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit(
            '%s: %s' % ('imio.facetednavigation', atype.portal_type),
            content_types=(atype, ),
            permission='plone.app.collection: Add Collection',
            extra_constructors=(constructor, ),
        ).initialize(context)
