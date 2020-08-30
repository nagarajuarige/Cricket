# Generated by Django 2.2.14 on 2020-08-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image_url',
            field=models.ImageField(default='media/images/players/default_image.png', upload_to='meadia/images/players/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo_url',
            field=models.ImageField(upload_to='media/images/teams/'),
        ),
    ]