# Generated by Django 5.2.1 on 2025-06-06 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_knowledgebase'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='knowledgebase',
            options={'verbose_name': 'Knowledge Base', 'verbose_name_plural': 'Knowledge Base'},
        ),
    ]
