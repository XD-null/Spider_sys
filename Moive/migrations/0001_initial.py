# Generated by Django 2.2.3 on 2019-07-30 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='电影名称')),
                ('real_time_gross', models.DecimalField(decimal_places=2, default=-1, max_digits=7, verbose_name='实时票房')),
                ('total_box_office', models.DecimalField(decimal_places=2, default=-1, max_digits=7, verbose_name='累计票房')),
                ('precent', models.DecimalField(decimal_places=2, default=-1, max_digits=4, verbose_name='实时排片')),
                ('row_screenings', models.IntegerField(max_length=7, verbose_name='实时场次')),
                ('Release_time', models.IntegerField(max_length=3, verbose_name='上映天数')),
            ],
            options={
                'verbose_name': '电影票房',
            },
        ),
    ]
