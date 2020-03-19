from django.contrib import admin
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'join_date')
    list_display_links = ('id', 'name')
    search_field = ('name')
    list_per_page = 25

admin.site.register(Agent, AgentAdmin)