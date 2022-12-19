# Generated by Django 4.1.4 on 2022-12-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='McUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('is_active', models.BooleanField()),
            ],
            options={
                'db_table': 'mcuser',
                'managed': False,
            },
        ),
    ]