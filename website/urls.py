from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import HeaderSitemap
from core.sitemaps import StaticViewSitemap
sitemaps = {
    'static': StaticViewSitemap ,

    'header':HeaderSitemap,
}
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns+= i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



