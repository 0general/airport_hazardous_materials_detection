# Generated by Django 4.0.4 on 2022-05-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash_view', '0003_detecteditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadfile',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('uploadedfile', models.FileField(upload_to='Uploaded_Files/')),
            ],
            options={
                'db_table': 'upload',
                'managed': False,
            },
        ),
    ]