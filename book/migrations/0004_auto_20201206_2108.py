# Generated by Django 3.1.3 on 2020-12-06 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0003_auto_20201121_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
