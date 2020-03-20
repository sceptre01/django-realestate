from django.shortcuts import render
from django.http import HttpResponse
from properties.models import Property
from agents.models import Agent
from properties.choices import price_choices, bedroom_choices, state_choices

# Create your views here.

def index(request):
    properties = Property.objects.order_by('-list_date').filter(is_published=True)[:6]
    agents = Agent.objects.order_by('-join_date')[:4]
    
    context = {
        'properties' : properties,
        'agents': agents,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
    }
    
    return render(request, 'pages/index.html', context)

def about(request):
    agents = Agent.objects.order_by('-join_date')[:4]
    
    context = {
        'agents': agents
    }
    return render(request, 'pages/about.html', context)

def faqs(request):
    return render(request, 'pages/faq.html')

def contact(request):
    return render(request, 'pages/contact.html')