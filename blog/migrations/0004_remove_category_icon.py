# Generated by Django 5.1.7 on 2025-03-07 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_created_at_category_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='icon',
        ),
    ]
