# Generated by Django 3.0.1 on 2020-03-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0003_auto_20200304_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
