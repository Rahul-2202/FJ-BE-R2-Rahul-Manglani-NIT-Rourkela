# Generated by Django 4.2.5 on 2023-09-13 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('+', 'Income'), ('-', 'Expense')], max_length=1)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='source',
        ),
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('+', 'Income'), ('-', 'Expense')], default='-', max_length=1),
        ),
        migrations.DeleteModel(
            name='IncomeSource',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.category'),
        ),
        migrations.DeleteModel(
            name='ExpenseCategory',
        ),
    ]