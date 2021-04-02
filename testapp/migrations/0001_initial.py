# Generated by Django 2.2.13 on 2021-04-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rollno', models.IntegerField()),
                ('age', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
