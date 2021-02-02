from django.contrib import admin

# Register your models here.
from portfolio.models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'results', 'rating', 'university', 'graduate')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'university', 'results')
    list_editable = ('rating', 'results')
    list_filter = ('university', 'rating')

admin.site.register(Portfolio, PortfolioAdmin)