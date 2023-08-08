# Generated by Django 2.2 on 2020-09-07 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20200908_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='content_type',
            field=models.CharField(help_text='The MIMEType of the file', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='picture',
            field=models.BinaryField(editable=True, null=True),
        ),
    ]