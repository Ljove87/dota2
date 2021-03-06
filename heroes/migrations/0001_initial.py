# Generated by Django 3.0.1 on 2020-01-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hero_type', models.CharField(choices=[('AGI', 'Agility'), ('INT', 'Intellect'), ('STR', 'Strength')], default='AGI', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Heroes',
            },
        ),
    ]
