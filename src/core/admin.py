from django.contrib import admin
from .models import Article,Comment
# Register your models here.

admin.site.register(Article)
admin.site.register(Comment)

'''
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','content','created','id')
	list_filter = ('title','content','created')
	ordering = ('publish',)
	prepopulated_fields = {'slug' :('title',)}
	search_fields = ('title','content')
'''