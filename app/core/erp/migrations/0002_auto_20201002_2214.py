# Generated by Django 3.1.2 on 2020-10-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d', verbose_name='Imagen'),
        ),
    ]
