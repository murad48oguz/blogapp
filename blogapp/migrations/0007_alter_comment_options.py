# Generated by Django 3.2.3 on 2021-09-17 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_remove_comment_approved_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_content']},
        ),
    ]
