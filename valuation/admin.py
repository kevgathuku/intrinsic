from django.contrib import admin

from .models import Company, Result


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')


class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'company', 'earnings', 'book_value', 'EPS',
        'current_ratio', 'debt_equity_ratio', 'results_url')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Result, ResultAdmin)
