# Generated by Django 4.0.2 on 2022-03-05 05:30

import blog_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_alter_newuser_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='user_image',
            field=models.ImageField(blank=True, upload_to=blog_app.models.NewUser.nameFile),
        ),
    ]