# -*- coding: utf-8 -*-

from medialog.globe import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class GlobeView(BrowserView):

    def results(self):
        return self.context.results()