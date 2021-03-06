# Generated by Django 3.1.4 on 2021-01-16 13:58

import accounts.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmationKey',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('key', models.CharField(default=accounts.utils.uuid, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('account_type', models.CharField(default='Standard', max_length=15)),
                ('birthday', models.DateField(blank=True, help_text='Birthday in YYYY-MM-DD format [used for displaying age].', null=True)),
                ('location', models.CharField(blank=True, help_text='Geographic location.', max_length=40)),
                ('website', models.URLField(blank=True, help_text='A personal blog or website.')),
                ('bio', models.TextField(blank=True, help_text='A brief biography.')),
            ],
            options={
                'ordering': ('-user__last_login',),
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('recipient', models.CharField(help_text='Registered user', max_length=150)),
                ('sender', models.CharField(max_length=150)),
                ('heading', models.CharField(blank=True, max_length=70, null=True)),
                ('text', models.TextField(max_length=9999)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('delete_image', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(default='Standard', max_length=15)),
                ('key', models.CharField(blank=True, max_length=20, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
    ]
