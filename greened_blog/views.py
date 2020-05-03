from django.shortcuts import render
from .models import Catlog, Article
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CatlogForm, ArticleForm

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')
# 后面就可以写 /pages/index.html 主页内容


def catlogs(request):
    catlogs = Catlog.objects.order_by('date_added')
    #context  = {'cats_1': cats_1}
    context  = {'catlogs': catlogs}
    return render(request, 'pages/catlogs.html', context)

def articles(request, catlog_id):
    catlog = Catlog.objects.get(id=catlog_id)
    articles = catlog.article_set.order_by('-date_added')
    context = {'catlog': catlog, 'articles': articles}
    return render(request, 'pages/articles.html', context)


def new_catlog(request):
    # 添加新主题
    if request.method != 'POST':
        # 如果未提交数据: 创建一个新表单
        form = CatlogForm()
    else:
        # POST 提交的数据. 对数据进行处理
        form = CatlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pages:catlogs'))  # 这里的参数不能有空格!!!
    context ={'form': form}
    return render(request, 'pages/new_catlog.html', context)


def new_article(request, catlog_id):
    # 特定目录中添加新的文章
    catlog = Catlog.objects.get(id=catlog_id)

    if request.method != 'POST':
        # 如果未提交数据: 创建一个新表单
        form = ArticleForm()
    else:
        # POST 提交的数据. 对数据进行处理
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.catlog = catlog
            new_article.save()
            return HttpResponseRedirect(reverse('pages:articles', args=[catlog_id])) #???
    context ={'catlog': catlog, 'form': form}
    return render(request, 'pages/new_article.html', context)


def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    catlog = article.catlog

    if request.method != 'POST':
        # 如果未提交数据: 创建一个新表单
        form = ArticleForm(instance=article)
    else:
        # POST 提交的数据. 对数据进行处理
        form = ArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('greened_blog:articles', args=[catlog.id])) # 这里和上面那个有什么关系?
    context ={'article': article, 'catlog': catlog, 'form': form}
    return render(request, 'pages/edit_article.html', context)

# 自动解析 URL
# url 触发的是 urls 中的 path
# path 将参数传递给 views 中的 function
# 经过函数对参数的解析, 函数会决定返回哪个页面, 并将 template 传递给页面




