# Generated by Django 5.1.4 on 2024-12-10 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('passwd', models.CharField(max_length=100, verbose_name='비밀번호')),
                ('username', models.CharField(max_length=10, verbose_name='글쓴이')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
            ],
            options={
                'verbose_name': '게시판',
                'verbose_name_plural': '게시판',
                'db_table': 'posts',
            },
        ),
    ]