# Generated by Django 4.2.3 on 2023-08-08 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalentPoolWeb', '0002_rename_individualuser_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
