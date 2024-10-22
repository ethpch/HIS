# Generated by Django 3.0.7 on 2020-06-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.IntegerField(max_length=10, primary_key=True, serialize=False, verbose_name='用户ID')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名称')),
                ('password', models.CharField(max_length=20, verbose_name='用户密码')),
                ('role', models.CharField(max_length=20, verbose_name='用户角色')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
    ]
