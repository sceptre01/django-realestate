from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Property

# Create your views here.
def index(request):
    properties = Property.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(properties, 3)

    page = request.GET.get('page')

    paged_properties = paginator.get_page(page)

    context= {
        'properties': paged_properties
    }
    return render(request, 'properties/properties.html', context)

def property(request, property_id):
    return render(request, 'properties/property.html')    

def search(request):
    return render(request, 'properties/search.html')    