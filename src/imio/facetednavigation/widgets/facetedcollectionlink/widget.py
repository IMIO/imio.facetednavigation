# encoding: utf-8

from eea.facetednavigation.widgets import ViewPageTemplateFile
from eea.facetednavigation.widgets.radio.widget import Widget as RadioWidget
from imio.facetednavigation.widgets.widget import FacetedCollectionBaseWidget


class Widget(FacetedCollectionBaseWidget, RadioWidget):

    widget_type = 'facetedcollection-link'
    widget_label = 'FacetedCollection Link'
    category_vocabulary = 'imio.facetednavigation.facetedcollectioncategoryvocabulary'

    index = ViewPageTemplateFile('widget.pt')

    view_js = '++resource++eea.facetednavigation.widgets.tagscloud.view.js'
    edit_js = '++resource++eea.facetednavigation.widgets.tagscloud.edit.js'
    view_css = '++resource++eea.facetednavigation.widgets.tagscloud.view.css'
    edit_css = '++resource++eea.facetednavigation.widgets.tagscloud.edit.css'
    css_class = 'faceted-tagscloud-widget'
