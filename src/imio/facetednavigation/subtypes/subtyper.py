from zope.interface import alsoProvides
from zope.interface import noLongerProvides
from zope.event import notify

from eea.facetednavigation.events import FacetedWillBeDisabledEvent
from eea.facetednavigation.events import FacetedWillBeEnabledEvent
from eea.facetednavigation.events import FacetedDisabledEvent
from eea.facetednavigation.events import FacetedEnabledEvent
from eea.facetednavigation.interfaces import IDisableSmartFacets
#from eea.facetednavigation.interfaces import IHidePloneLeftColumn
from eea.facetednavigation.interfaces import IHidePloneRightColumn
from eea.facetednavigation.subtypes.subtyper import FacetedSubtyper

from imio.facetednavigation import ImioFacetedMessageFactory as _
from imio.facetednavigation.interfaces import ICollectionFacetApplied


class ImioFacetedSubtyper(FacetedSubtyper):

    def enable(self):
        """ See IFacetedSubtyper from eea.facetednavigation.subtypes """
        if not self.can_enable:
            return self._redirect('Faceted navigation not supported')

        notify(FacetedWillBeEnabledEvent(self.context))
        alsoProvides(self.context, ICollectionFacetApplied)
        if not IDisableSmartFacets.providedBy(self.context):
            alsoProvides(self.context, IDisableSmartFacets)
        if not IHidePloneRightColumn.providedBy(self.context):
            alsoProvides(self.context, IHidePloneRightColumn)
        notify(FacetedEnabledEvent(self.context))

        self._redirect(_('Faceted navigation enabled'))

    def disable(self):
        """ See IFacetedSubtyper from eea.facetednavigation.subtypes """
        if not self.can_disable:
            return self._redirect('Faceted navigation not supported')

        notify(FacetedWillBeDisabledEvent(self.context))
        noLongerProvides(self.context, ICollectionFacetApplied)
        notify(FacetedDisabledEvent(self.context))
        self._redirect(_('Faceted navigation disabled'))
