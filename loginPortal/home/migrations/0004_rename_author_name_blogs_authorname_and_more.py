# Generated by Django 4.1.1 on 2022-09-20 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_auth_blogs_author_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='Author_name',
            new_name='Authorname',
        ),
        migrations.RenameField(
            model_name='blogs',
            old_name='Title',
            new_name='title',
        ),
    ]
