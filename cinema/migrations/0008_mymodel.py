# Generated by Django 4.0.4 on 2024-04-18 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_alter_moviesession_show_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage='django.core.files.storage.FileSystemStorage', upload_to='')),
            ],
        ),
    ]