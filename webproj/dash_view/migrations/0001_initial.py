# Generated by Django 3.2.13 on 2022-04-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noti',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('timestamp', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'DASHVIEW_NOTIFY',
                'managed': False,
            },
        ),
    ]
