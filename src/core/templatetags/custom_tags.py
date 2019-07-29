from django import template
from django.db.models import Count
from core.models import Article
register = template.Library()

@register.simple_tag
def total_articles():
	return Article.objects.count()

@register.inclusion_tag('core/custom-tag/latest_articles.html')
def latest_articles(num=3):
	articles = Article.objects.order_by('-created')[:num]
	return {'articles':articles}

@register.inclusion_tag('core/custom-tag/commented_articles.html')
def most_commented_articles(num=3):
	articles = Article.objects.annotate(commented_articles = Count('comments')).order_by('-commented_articles')[:num]
	return {'articles' :articles}

