from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from .models import Document


class LatestFeed(Feed):
    title = "젤리의 망상 최근 Feeds"
    link = "/blognews/"
    description = "젤리의 망상의 피드입니다."

    def items(self):
        return Document.objects.filter(public_doc=True).order_by('-time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('detail', args=[item.pk])


class AllPublickFeed(Feed):
    title = "젤리의 망상 Feeds"
    link = "/blognews/"
    description = "젤리의 망상 Feeds"

    def items(self):
        return Document.objects.filter(public_doc=True).order_by('-time')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('detail', args=[item.pk])
    
