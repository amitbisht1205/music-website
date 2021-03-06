# Generated by Django 4.0 on 2022-01-27 05:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'], 'allow.images')]),
        ),
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['mp3', 'aac', 'amr', 'wav'], 'allow.mp3')]),
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])])),
                ('address', models.TextField(max_length=100)),
                ('intrest', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('u_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
