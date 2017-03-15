from __future__ import division

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=5, blank=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __unicode__(self):
        return self.name


class Result(models.Model):
    """
    Stores a Company's Declared Results for a Specific Accounting Period
    """

    results_url = models.URLField(blank=True, null=True)

    PERIOD_CHOICES = (
        (6, '6 Months'),
        (9, '9 Months'),
        (12, 'Full Year'),
    )

    period_end_date = models.DateField()
    period_length = models.IntegerField(
        choices=PERIOD_CHOICES,
        # Set default explicitly from the PERIOD_CHOICES tuple (12 months)
        default=PERIOD_CHOICES[2][0],
        help_text="Length of the period for which the results belong to")

    company = models.ForeignKey(Company, unique_for_date='period_end_date')

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
