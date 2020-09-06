from django.shortcuts import render
from .models import Phone
from django.shortcuts import get_object_or_404


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort_by')
    phones = Phone.objects.all()
    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'price_a':
        phones = phones.order_by('price')
    elif sort == 'price_d':
        phones = phones.order_by('-price')

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': get_object_or_404(Phone, slug=slug)
    }
    return render(request, template, context)
