from django.conf.urls import patterns, include, url

urlpatterns = patterns('calisphere',
    url(r'^$', 'views.search', name='search'),
    url(r'^(?P<item_id>.*)/', 'views.itemView', name='itemView'),
    url(r'^collections/$', 'views.collectionsExplore', name='collectionsExplore'),
    url(r'^collections/(?P<collection_id>.*)/', 'views.collectionView', name='collectionView'),
)