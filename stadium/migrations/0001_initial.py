# Generated by Django 3.2.16 on 2024-01-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=255)),
                ('stadium', models.CharField(max_length=255)),
                ('stadium_image', models.ImageField(blank=True, null=True, upload_to='stadium_images/')),
            ],
        ),
    ]