# Generated by Django 4.2.3 on 2023-10-07 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='protfolio_site',
            new_name='portfolio_site',
        ),
    ]
