# Generated by Django 3.2.19 on 2023-06-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='书籍名称')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('pub_date', models.DateField(verbose_name='出版日期')),
            ],
        ),
    ]
