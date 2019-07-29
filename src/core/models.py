from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.


class PublishManager(models.Manager):
	def get_queryset(self):
		return super(PublishManager,self).get_queryset().filter(slug="hello-django")



class Article(models.Model):
	PUBLISH_CHOICES = (
		('D','Draft'),('P','publish')
	)
	title =  models.CharField(max_length=100)
	user = models.ForeignKey(User,related_name='articles',on_delete=models.CASCADE)
	content = models.TextField()
	slug = models.SlugField()
	created= models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	publish = models.DateTimeField(default = timezone.now)
	status = models.CharField(choices=PUBLISH_CHOICES,max_length=1,default='D')
	objects = models.Manager()
	published = PublishManager()

	tags = TaggableManager()
	class Meta:
		ordering = ('-publish',)

	def get_absolute_url(self):
		return reverse('core:detail', kwargs={'id':self.id,'slug':self.slug})

	def __str__(self):
		return self.title



class Comment(models.Model):
	article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('created',)
	def __str__(self):
		return "{} comment on {}".format(self.name,self.article)










