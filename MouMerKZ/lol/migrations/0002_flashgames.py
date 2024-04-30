# Generated by Django 4.2.6 on 2024-04-27 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlashGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='games/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flash_games', to='lol.lol')),
            ],
        ),
    ]
