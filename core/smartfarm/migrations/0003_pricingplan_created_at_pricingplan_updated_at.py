# Generated by Django 4.1.3 on 2022-11-16 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartfarm', '0002_pricingplan_delete_farmer'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricingplan',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='pricingplan',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
