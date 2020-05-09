from django import forms

from .models import Catlog, Article

class CatlogForm(forms.ModelForm):
    class Meta:
        model = Catlog
        fields = ['text']
        labels = {'text': ''}

class ArticleForm(forms.ModelForm):
    class Meta:
    #这里的模型是 Article
        model = Article
        fields = [ 'header', 'body' ]
        labels = { 'header':'', 'body':'' }
        # widget = CKEditorWidget(config_name='awesome_ckeditor')



