# Generated by Django 2.2.7 on 2019-12-03 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_removed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='removed',
            field=models.NullBooleanField(),
        ),
    ]
