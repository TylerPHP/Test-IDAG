# Generated by Django 3.0.8 on 2020-07-03 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_hash', models.CharField(max_length=150)),
                ('add_date', models.DateTimeField(default='2020-07-03 19:39:13', max_length=140)),
                ('uploade_date', models.DateTimeField(default='2020-07-03 19:39:13', max_length=140)),
            ],
        ),
    ]