from django.contrib import admin

# Register your models here.
from .models import Company, BalanceSheet, IncomeStatement

admin.site.register(Company)
admin.site.register(BalanceSheet)
admin.site.register(IncomeStatement)
