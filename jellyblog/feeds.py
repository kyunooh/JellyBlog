# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from .models import Document

class LatestFeed(Feed):
    title = "젤리의 망상 Feeds"
    link = "/blognews/"
    description = "젤리의 망상의 피드입니다."

    def items(self):
        return Document.objects.order_by('-time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('detail', args=[item.pk])
