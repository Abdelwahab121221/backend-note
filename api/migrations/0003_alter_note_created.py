# Generated by Django 5.0.6 on 2024-07-03 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_note_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]