# Generated by Django 4.2.5 on 2023-10-12 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_product_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='detail',
            new_name='description',
        ),
    ]