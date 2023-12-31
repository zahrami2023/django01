# Generated by Django 4.2.4 on 2023-10-20 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_education_experience_alter_userprofile_picture'),
        ('blog', '0004_post_dislike_post_like_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='post_dislike', to='accounts.userprofile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='post_like', to='accounts.userprofile'),
        ),
    ]
