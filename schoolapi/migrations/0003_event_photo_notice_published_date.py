# Generated by Django 4.0.3 on 2022-03-25 07:47

from django.db import migrations, models
import django.utils.timezone
import schoolapi.models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapi', '0002_teacher_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=schoolapi.models.name_of_image),
        ),
        migrations.AddField(
            model_name='notice',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
