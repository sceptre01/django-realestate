from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='agents'),
    path('<int:agent_id>', views.agent, name='agent')
]