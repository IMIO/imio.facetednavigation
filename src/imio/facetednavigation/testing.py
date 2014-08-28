# encoding: utf-8

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class ImiofacetednavigationLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import imio.facetednavigation
        xmlconfig.file(
            'configure.zcml',
            imio.facetednavigation,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'imio.facetednavigation:default')

IMIO_FACETEDNAVIGATION_FIXTURE = ImiofacetednavigationLayer()
IMIO_FACETEDNAVIGATION_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IMIO_FACETEDNAVIGATION_FIXTURE,),
    name="ImiofacetednavigationLayer:Integration"
)
IMIO_FACETEDNAVIGATION_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(IMIO_FACETEDNAVIGATION_FIXTURE, z2.ZSERVER_FIXTURE),
    name="ImiofacetednavigationLayer:Functional"
)
