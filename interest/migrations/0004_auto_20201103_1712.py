# Generated by Django 2.2.2 on 2020-11-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0003_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
