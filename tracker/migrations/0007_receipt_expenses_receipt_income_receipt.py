# Generated by Django 4.2.5 on 2023-09-14 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0006_sharedexpense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('receipt_image', models.ImageField(upload_to='receipts/')),
                ('expenses_transactions', models.ManyToManyField(blank=True, related_name='receipts', to='tracker.expenses')),
                ('income_transactions', models.ManyToManyField(blank=True, related_name='receipts', to='tracker.income')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='expenses',
            name='receipt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracker.receipt'),
        ),
        migrations.AddField(
            model_name='income',
            name='receipt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracker.receipt'),
        ),
    ]
