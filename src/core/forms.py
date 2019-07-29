from django import forms
from .models import Comment
class SendEmailForm(forms.Form):
	name = forms.CharField(max_length=50)
	email = forms.EmailField()
	subject = forms.CharField(max_length=50)
	message = forms.CharField(widget=forms.Textarea,required=False)


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('content',)
		

class SearchForm(forms.Form):
	q = forms.CharField(max_length=50)
	