# Generated by Django 4.1.7 on 2023-03-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0005_alter_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
