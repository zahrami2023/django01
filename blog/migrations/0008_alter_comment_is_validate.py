# Generated by Django 4.2.4 on 2023-10-26 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_dislike_alter_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_validate',
            field=models.BooleanField(null=True),
        ),
    ]
