from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
import markdown
import pygments
from blog.utils.pager import Pagination
from django.db.models import Q
# Create your views here.



def index(request):
    page = request.GET.get('page', 1)
    total_count = models.Entry.objects.all().count()  #
    pager = Pagination(page, total_count, reverse('blog:blog_index'))
    depart_queryset = models.Entry.objects.all()[pager.start:pager.end]
    return render(request, 'blog/index.html', locals())

def detail(request,blog_id):

    entry = models.Entry.objects.get(id=blog_id)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    entry.body = md.convert(entry.body)
    entry.toc = md.toc
    entry.created_viting()
    return render(request, 'blog/detail.html', locals())

def category(request,category_id):
    c = models.Category.objects.get(id=category_id)
    entries = models.Entry.objects.filter(category=c)
    page = request.GET.get('page', 1)
    total_count = entries.count()  #
    pager = Pagination(page, total_count, reverse('blog:blog_category',kwargs={"category_id":category_id}))
    depart_queryset = entries[pager.start:pager.end]
    return render(request, 'blog/index.html', locals())


def tag(request,tag_id):
    t = models.Tag.objects.get(id=tag_id)
    entries = models.Entry.objects.filter(tags=t)
    page = request.GET.get('page', 1)
    total_count = entries.count()  #
    pager = Pagination(page, total_count, reverse('blog:blog_tag',kwargs={'tag_id':tag_id}))
    depart_queryset = entries[pager.start:pager.end]
    return render(request, 'blog/index.html', locals())


def search(request):

    keyword = request.GET.get('keyword', None)
    if not keyword or str(keyword) == '':
        error_msg = "请输入关键字"
        #跳转首页
        return redirect('blog:blog_index')

    entries = models.Entry.objects.filter(Q(title__icontains=keyword)
                                          | Q(body__icontains=keyword)
                                          | Q(abstract__icontains=keyword))
    page = request.GET.get('page', 1)
    total_count = entries.count()  #
    depart_queryset = entries
    return render(request, 'blog/index.html', locals())


def archives(request,year,month):
    entris = models.Entry.objects.filter(created_time__year=year, created_time__month=month)
    page = request.GET.get('page', 1)
    total_count = entris.count()  #
    pager = Pagination(page, total_count, reverse('blog:blog_archives', kwargs={'year':year,'month':month}))
    depart_queryset = entris[pager.start:pager.end]
    return render(request, 'blog/index.html', locals())