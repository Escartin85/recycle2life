# Generated by Django 3.0.3 on 2020-03-08 22:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(max_length=1500)),
                ('priority', models.CharField(max_length=10)),
                ('location_country', models.CharField(max_length=50)),
                ('location_city', models.CharField(max_length=50)),
                ('location_postcode', models.CharField(max_length=10)),
                ('typeAd', models.CharField(max_length=10)),
                ('external', models.BooleanField(default=False)),
                ('external_link', models.CharField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('date_external', models.DateTimeField(blank=True, null=True)),
                ('likes', models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(99999)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
