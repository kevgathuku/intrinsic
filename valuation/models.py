from django.db import models

DURATION_CHOICES = (
    (3, '3 Months'),
    (6, 'Half Year'),
    (9, '9 Months'),
    (12, 'Full Year'),
)

class Company(models.Model):
    """
    A company whose shares are traded in the Stock Exchange
    """

    name = models.CharField(max_length=250)
    symbol = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)

    year_end = models.DateField(blank=True)
    outstanding_shares = models.BigIntegerField(blank=True, default=0)
    investor_relations_link = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class BalanceSheet(models.Model):
    """A company's balance sheet for a specific financial period"""

    date = models.DateField()
    duration = models.PositiveSmallIntegerField(
        choices=DURATION_CHOICES,
        # Set default explicitly from the DURATION_CHOICES tuple (12 months)
        default=DURATION_CHOICES[3][0],
        help_text="Financial Period which the results belong to")

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    equity = models.BigIntegerField(help_text="Shareholders' Equity", blank=True, default=0)
    liabilities = models.BigIntegerField(help_text="Total Liabilities", blank=True, default=0)
    assets = models.BigIntegerField(help_text="Total Assets", blank=True, default=0)

    debt = models.BigIntegerField(help_text="Total Borrowed Funds", blank=True, default=0)

    current_assets = models.BigIntegerField(blank=True, default=0)
    current_liabilities = models.BigIntegerField(blank=True, default=0)

    @property
    def current_ratio(self):
        return self.current_assets / self.current_liabilities

    @property
    def debt_equity_ratio(self):
        return self.debt / self.equity

    def __str__(self):
        return "{}: Balance Sheet for the {} months ending {:%d %B %Y}".format(
            self.company.name,
            self.duration,
            self.date)


class IncomeStatement(models.Model):
    """A company's income statement for a specific financial period"""

    date = models.DateField()
    duration = models.PositiveSmallIntegerField(
        choices=DURATION_CHOICES,
        # Set default explicitly from the DURATION_CHOICES tuple (12 months)
        default=DURATION_CHOICES[3][0],
        help_text="Length of the period for which the results belong to")

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    total_revenue = models.BigIntegerField(blank=True, default=0)
    operating_expenses = models.BigIntegerField(blank=True, default=0)

    profit_before_tax = models.BigIntegerField(help_text="Profit before tax and exceptional items", blank=True, default=0)
    exceptional_items = models.BigIntegerField(blank=True, default=0)
    net_income = models.BigIntegerField(help_text="Profit after tax for the period", blank=True, default=0)

    @property
    def eps(self):
        return self.net_income / self.company.outstanding_shares

    def __str__(self):
        return "{}: Income Statement for the {} months ending {:%d %B %Y}".format(
            self.company.name,
            self.duration,
            self.date)
