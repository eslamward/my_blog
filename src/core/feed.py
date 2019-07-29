from django.template.defaultfilters import truncatewords
from django.contrib.syndication.views import Feed
from .models import Article

class LatesFiveArticleFeed(Feed):
	title= 'Articles'
	link= '/article/'
	description = 'Latest Five Article Feed'

	def items(self):
		return Article.objects.all()[:5]

	def item_title(self,obj):
		return obj.title

	def item_description(self,obj):
		return truncatewords(obj.content,50)