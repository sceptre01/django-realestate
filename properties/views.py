from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Property
from agents.models import Agent
from .choices import price_choices, bedroom_choices, state_choices



# Create your views here.
def index(request):
    properties = Property.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(properties, 6)

    page = request.GET.get('page')

    paged_properties = paginator.get_page(page)

    context= {
        'properties': paged_properties
    }
    return render(request, 'properties/properties.html', context)

def property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    agents = Agent.objects.filter(name=property.agent)

    context = {
        'property': property,
        'agents': agents
    }

    return render(request, 'properties/property.html', context)    

def search(request):

    queryset_list = Property.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)


    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'properties': queryset_list,
        'values' : request.GET
    }
    return render(request, 'properties/search.html', context)    