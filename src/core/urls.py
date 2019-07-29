from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ArticleSitemap
from .feed import LatesFiveArticleFeed
from .views import article_list,article_detail,send_message
app_name='core'


sitemaps = {
	'article':ArticleSitemap
}
urlpatterns = [

	path('',article_list,name='list'),
	path('<slug:tag_name>',article_list,name='list_by_tag'),
	path('<slug:slug>/<int:id>/',article_detail,name='detail'),
	path('<slug:slug>/<int:id>/share',send_message,name='send_message'),
	path('sitemapfile.xml',sitemap,{'sitemaps':sitemaps},\
		name = 'django.contrib.sitemaps.views.sitemap'),
	path('feed/',LatesFiveArticleFeed(),name='feed')
]