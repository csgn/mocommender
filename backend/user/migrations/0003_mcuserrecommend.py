# Generated by Django 4.1.4 on 2022-12-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_mcusermovie'),
    ]

    operations = [
        migrations.CreateModel(
            name='McUserRecommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'mcuserrecommend',
                'managed': False,
            },
        ),
    ]