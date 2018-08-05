from __future__ import division

from django.db import models


class Company(models.Model):
    """
    Represents a Company whose shared are traded in the Stock Exchange
    """

    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=5, blank=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __unicode__(self):
        return self.name


class FinancialPeriod(models.Model):
    DURATION_CHOICES = (
        (3, '3 Months'),
        (6, 'Half Year'),
        (9, '9 Months'),
        (12, 'Full Year'),
    )

    end_date = models.DateField()
    duration = models.IntegerField(
        choices=DURATION_CHOICES,
        # Set default explicitly from the DURATION_CHOICES tuple (12 months)
        default=DURATION_CHOICES[2][0],
        help_text="Length of the period for which the results belong to")

    def __unicode__(self):
        return "Results for the {} financial period ended {:%d %B %Y}".format(
            self.duration,
            self.end_date)


class BalanceSheet(models.Model):
    """Represents a company's balance sheet portion of results"""

    company = models.ForeignKey(Company)
    results_url = models.URLField(blank=True, null=True)
    financial_period = models.ForeignKey(FinancialPeriod)


class IncomeStatement(models.Model):
    """Represents a company's income statement portion of results"""

    company = models.ForeignKey(Company)
    results_url = models.URLField(blank=True, null=True)
    financial_period = models.ForeignKey(FinancialPeriod)

    revenue = models.IntegerField()
    other_revenue = models.IntegerField()
    cost_of_revenue = models.IntegerField()

    operating_expenses = models.IntegerField()

    non_operating_income = models.IntegerField()
    other_income = models.IntegerField()

    provision_for_income_taxes = models.IntegerField()

    extraordinary_items = models.IntegerField(blank=True, default=0)

    @property
    def gross_profit(self):
        return (self.revenue + self.other_revenue) - self.cost_of_revenue

    @property
    def operating_income(self):
        return self.gross_profit - self.operating_expenses

    @property
    def net_income_before_taxes(self):
        return self.operating_income + \
            (self.non_operating_income + self.other_income)

    @property
    def net_income_after_taxes(self):
        return self.net_income_before_taxes - self.provision_for_income_taxes

    @property
    def net_income(self):
        return self.net_income_after_taxes - self.extraordinary_items


class Result(models.Model):
    """
    Stores a Company's Declared Results for a Specific Accounting Period
    """

    results_url = models.URLField(blank=True, null=True)

    company = models.ForeignKey(Company)

    earnings = models.IntegerField(help_text="Profit after tax for the period")
    debt = models.IntegerField(
        help_text="Total Borrowed Funds", blank=True, null=True)

    equity = models.IntegerField(help_text="Shareholders' Equity")
    current_assets = models.IntegerField()
    current_liabilities = models.IntegerField()

    EPS = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="profit attributable to equity \
        holders of the Company divided by outstanding shares")
    outstanding_shares = models.IntegerField(
        help_text="Total Number of Issued shares")

    book_value = models.DecimalField(max_digits=7, decimal_places=2)

    @property
    def current_ratio(self):
        return self.current_assets / self.current_liabilities

    @property
    def debt_equity_ratio(self):
        return self.debt / self.equity

    def __unicode__(self):
        return "{}: Results for the {} month period ended {:%d %B %Y}".format(
            self.company.name,
            self.period_length,
            self.period_end_date)
