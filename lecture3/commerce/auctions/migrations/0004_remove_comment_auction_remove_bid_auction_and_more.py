# Generated by Django 5.0.6 on 2024-09-18 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.DeleteModel(
            name='Auction',
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]