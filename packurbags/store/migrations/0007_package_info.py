# Generated by Django 4.1.5 on 2023-01-19 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='info',
            field=models.TextField(null=True),
        ),
    ]
