# Generated by Django 5.0.2 on 2024-04-20 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipies_list_app', '0002_rename_recipies_data_recipe_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipe',
            new_name='recipies_data',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
