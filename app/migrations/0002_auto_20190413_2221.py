# Generated by Django 2.2 on 2019-04-13 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-username'],
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-username']},
        ),
    ]
