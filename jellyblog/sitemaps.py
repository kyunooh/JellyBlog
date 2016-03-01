# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from .models import Document


class BlogSitemap(Sitemap):
    changefreq = "hourly"
    priority = 1.0

    def items(self):
        return Document.objects.filter(public_doc=True)

    def lastmod(self, obj):
        return obj.update_time
