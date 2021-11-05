# Generated by Django 3.2.9 on 2021-11-05 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('date_of_join', models.DateField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]
