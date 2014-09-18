# encoding: utf-8

from eea.facetednavigation.widgets import ViewPageTemplateFile
from eea.facetednavigation.widgets.radio.widget import Widget as RadioWidget
from imio.facetednavigation.widgets.widget import FacetedCollectionBaseWidget


class Widget(FacetedCollectionBaseWidget, RadioWidget):

    widget_type = 'facetedcollection-radio'
    widget_label = 'FacetedCollection Radio'
    category_vocabulary = 'imio.facetednavigation.facetedcollectioncategoryvocabulary'

    index = ViewPageTemplateFile('widget.pt')
