# Generated by Django 3.1.6 on 2021-05-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='identifier',
            field=models.IntegerField(blank=True, default=8888),
            preserve_default=False,
        ),
    ]
