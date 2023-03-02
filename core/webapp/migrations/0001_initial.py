# Generated by Django 4.1.7 on 2023-03-01 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=100, verbose_name='Краткое описание')),
                ('description', models.TextField(max_length=2500, null=True, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.status')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.type')),
            ],
        ),
    ]