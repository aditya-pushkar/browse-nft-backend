# Generated by Django 4.0.3 on 2022-03-04 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nft',
            fields=[
                ('username', models.CharField(blank=True, max_length=500)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('decription', models.CharField(max_length=300, unique=True)),
                ('img', models.URLField(max_length=2000)),
                ('eth_price', models.DecimalField(decimal_places=3, max_digits=9)),
                ('redirect_link', models.URLField(max_length=2000)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='tags', to='nft.tag')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
