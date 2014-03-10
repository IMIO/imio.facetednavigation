# encoding: utf-8
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from imio.facetednavigation import ImioFacetedMessageFactory as _
from imio.facetednavigation.interfaces import ICollectionFacetApplied


class IFacetedCollectionPortlet(IPortletDataProvider):
    """ A portlet that shows controls for faceted with collections """


class Assignment(base.Assignment):
    implements(IFacetedCollectionPortlet)

    def __init__(self):
        pass

    @property
    def title(self):
        return _(u"Collections")


class Renderer(base.Renderer):

    def render(self):
        return ViewPageTemplateFile('templates/portlet_collection.pt')(self)

    @property
    def available(self):
        return ICollectionFacetApplied.providedBy(self.context)

    @property
    def collections(self):
        pass


class AddForm(base.AddForm):
    form_fields = form.Fields(IFacetedCollectionPortlet)
    label = _(u"Add Collection Criteria Portlet")
    description = _(u"This portlet shows controls for faceted with collections.")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(IFacetedCollectionPortlet)
    label = _(u"Edit Collection Criteria Portlet")
    description = _(u"This portlet shows controls for faceted with collections.")
