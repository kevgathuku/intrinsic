# Generated by Django 3.0.5 on 2020-04-09 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('symbol', models.CharField(blank=True, max_length=50)),
                ('bio', models.TextField(blank=True)),
                ('year_end', models.DateField(blank=True)),
                ('outstanding_shares', models.BigIntegerField(blank=True, default=0)),
                ('investor_relations_link', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='IncomeStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration', models.PositiveSmallIntegerField(choices=[(3, '3 Months'), (6, 'Half Year'), (9, '9 Months'), (12, 'Full Year')], default=9, help_text='Length of the period for which the results belong to')),
                ('total_revenue', models.BigIntegerField(blank=True, default=0)),
                ('operating_expenses', models.BigIntegerField(blank=True, default=0)),
                ('profit_before_tax', models.BigIntegerField(blank=True, default=0, help_text='Profit before tax and exceptional items')),
                ('exceptional_items', models.BigIntegerField(blank=True, default=0)),
                ('net_income', models.BigIntegerField(blank=True, default=0, help_text='Profit after tax for the period')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuation.Company')),
            ],
        ),
        migrations.CreateModel(
            name='BalanceSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration', models.PositiveSmallIntegerField(choices=[(3, '3 Months'), (6, 'Half Year'), (9, '9 Months'), (12, 'Full Year')], default=9, help_text='Financial Period which the results belong to')),
                ('equity', models.BigIntegerField(help_text="Shareholders' Equity")),
                ('liabilities', models.BigIntegerField(help_text='Total Liabilities')),
                ('assets', models.BigIntegerField(help_text='Total Assets')),
                ('debt', models.BigIntegerField(blank=True, default=0, help_text='Total Borrowed Funds')),
                ('current_assets', models.BigIntegerField(blank=True, default=0)),
                ('current_liabilities', models.BigIntegerField(blank=True, default=0)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuation.Company')),
            ],
        ),
    ]