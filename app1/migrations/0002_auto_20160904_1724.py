# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='a',
            old_name='field1',
            new_name='nombre',
        ),
        migrations.AddField(
            model_name='b',
            name='a',
            field=models.ForeignKey(to='app1.A'),
        ),
    ]
