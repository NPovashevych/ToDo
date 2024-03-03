# Generated by Django 5.0.2 on 2024-03-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('deadline_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('tag', models.ManyToManyField(related_name='tasks', to='tasks.tag')),
            ],
            options={
                'ordering': ('-created_time',),
            },
        ),
    ]
