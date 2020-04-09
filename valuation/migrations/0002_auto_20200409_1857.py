# Generated by Django 3.0.5 on 2020-04-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valuation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancesheet',
            name='assets',
            field=models.BigIntegerField(blank=True, default=0, help_text='Total Assets'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='duration',
            field=models.PositiveSmallIntegerField(choices=[(3, '3 Months'), (6, 'Half Year'), (9, '9 Months'), (12, 'Full Year')], default=12, help_text='Financial Period which the results belong to'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='equity',
            field=models.BigIntegerField(blank=True, default=0, help_text="Shareholders' Equity"),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='liabilities',
            field=models.BigIntegerField(blank=True, default=0, help_text='Total Liabilities'),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='duration',
            field=models.PositiveSmallIntegerField(choices=[(3, '3 Months'), (6, 'Half Year'), (9, '9 Months'), (12, 'Full Year')], default=12, help_text='Length of the period for which the results belong to'),
        ),
    ]
