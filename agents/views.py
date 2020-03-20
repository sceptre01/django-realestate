from django.shortcuts import render, get_object_or_404
from .models import Agent

# Create your views here.
def index(request):
    agents = Agent.objects.order_by('-join_date')

    context= {
        'agents': agents
    }
    return render(request, 'agents/agents.html', context)

def agent(request, agent_id):

    agent = get_object_or_404(Agent, pk=agent_id)

    context = {
        'agent' : agent
    }

    return render(request, 'agents/agent.html', context)    
