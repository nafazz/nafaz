from django.contrib.sitemaps import Sitemap
#from django.contrib.sitemaps.views import sitemap # new
from .models import Header
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    i18n = True

    def items(self):
        return ['home']
    def location(self, item):
        return reverse(item)
class HeaderSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    i18n = True

    protocol = 'http'
    def items(self):
        return Header.objects.all()