from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail
from .models import Article,Comment
from .forms import SendEmailForm,CommentForm,SearchForm
from taggit.models import Tag
from django.db.models import Count

# Create your views here.
def article_list(request,tag_name=None):
	obj_list = Article.objects.all()

	if tag_name:
		tag = get_object_or_404(Tag,name=tag_name)
		obj_list = Article.objects.filter(tags__in=[tag])
	paginator = Paginator(obj_list,3)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	print(page)
	context = {'articles':articles,'page':page}

	return render(request,'core/list.html',context)


def article_detail(request,id,slug):
	article = get_object_or_404(Article,slug=slug,id=id,status='P')
	tags_name = article.tags.values_list('slug',flat=True)
	print(tags_name)
	similar_articles = Article.objects.filter(tags__name__in=tags_name).exclude(id=article.id)
	similar_articles = similar_articles.annotate(tags_num=Count('tags')).order_by('-tags_num','-publish')[:3]
	
	comments = article.comments.all()

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.article = article
			comment.user = request.user
			comment.save()
			return redirect(article.get_absolute_url())
	else:
		form = CommentForm()
	context = {'article':article,'comments':comments,'form':form,'similar_articles':similar_articles}
	return render(request,'core/detail.html',context)



def send_message(request,slug,id):
	article = get_object_or_404(Article,slug=slug,id = id,status="P")
	sent = False

	if request.method == "POST":
		form = SendEmailForm(request.POST)
		if form.is_valid():
			cleaned_data = form.cleaned_data
			subject = cleaned_data['subject']
			to      = cleaned_data['email']
			name    = cleaned_data['name']
			message = cleaned_data['message']
			url = request.build_absolute_uri(article.get_absolute_url())
			message = message + 'Article Link'+ '>>>>' + url

			send_mail(subject,message,'worldwideweb363@gmail.com',[to],fail_silently=False)
			sent = True
			print(True)
	else:
		form = SendEmailForm()
	context = {'form':form,'sent':sent}
	return render(request,'core/message.html',context)




