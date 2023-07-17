# Generated by Django 4.0.6 on 2023-07-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Quiz question'), (1, 'Describe the picture'), (2, 'Build a story')]),
        ),
    ]
