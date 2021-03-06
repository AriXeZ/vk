# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models import Q
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from .models import Product, Section, Order, Article
from .utils import GET_SITE_PREFS

def index(request):
    return HttpResponseRedirect(GET_SITE_PREFS().main_page_redirect)


def section(request, slug):
    s = get_object_or_404(Section, slug=slug)
    qs_products = s.products.filter(
        retailcrm_id__isnull=False
    )
    items = (
        list(qs_products.filter(
            Q(in_stock=True) | Q(preorder__isnull=False) | Q(is_market_test=True)
        ))
        + list(qs_products.filter(in_stock=False, preorder__isnull=True, is_market_test=False))
    )
    return render(request, 'section.html', {
        'section': s,
        'menu': 'section-{}'.format(s.id),
        'items': items,
        # common items
        'header_id': s.header_id,
    })


def product(request, id, slug=None):
    p = get_object_or_404(Product, id=id)
    if slug != p.slug:
        return HttpResponseRedirect(u'/product/{}/{}/'.format(p.id, p.slug))
    return render(request, 'product.html', {
        'product': p,
        'menu': 'product-{}'.format(p.id),
        # common items
        'header_id': 'header01',
    })


def discount(request):
    qs = Product.objects.filter(
        retailcrm_id__isnull=False,
        discount_price__isnull=False,
    )
    items = (
        list(qs.filter(in_stock=True, is_new=True)) +
        list(qs.filter(in_stock=True, is_new=False)) +
        list(qs.filter(in_stock=False))
    )
    return render(request, 'discount.html', {
        'items': items,
        'menu': 'discount',
        # common items
        'header_id': 'header02',
    })


def article(request, id, slug=None):
    a = get_object_or_404(Article, id=id)
    if slug != a.slug:
        return HttpResponseRedirect(u'/a/{}/{}/'.format(a.id, a.slug))
    return render(request, 'article.html', {
        'article': a,
        'menu': 'articles',
    })

def article_list(request):
    return render(request, 'article_list.html', {
        'articles': Article.objects.filter(enabled=True).order_by('-created_at'),
        'menu': 'articles',
    })


from django.db import transaction
from django.contrib.auth.decorators import login_required
from .sync import sync_prices, sync_new_items, sync_fields, collect_sync_data


@login_required()
@transaction.atomic()
def sync(request):
    data = collect_sync_data()

    if request.method == 'POST':
        if request.POST.get('sync-prices'):
            sync_prices(data['common'], data['plist_f'])
        if request.POST.get('sync-fields'):
            sync_fields()
        if request.POST.get('sync-items'):
            sync_new_items()
        return HttpResponseRedirect('/sync/')

    return render(request, 'sync.html', data)
