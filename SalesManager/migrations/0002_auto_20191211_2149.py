# Generated by Django 3.0 on 2019-12-11 18:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SalesManager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='producer_link',
        ),
        migrations.AddField(
            model_name='product',
            name='expiration_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='expiration date'),
        ),
        migrations.AddField(
            model_name='storage',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='storageaction',
            name='action_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='real date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='batch_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date of sold'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=models.DecimalField(decimal_places=2, max_digits=6), max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='SalesManager.Storage'),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage_action',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='SalesManager.StorageAction'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='last_edition',
            field=models.DateTimeField(auto_now=True, verbose_name='edition date'),
        ),
        migrations.AlterField(
            model_name='storageaction',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='storageaction',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='SalesManager.Storage'),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('producer_link', models.URLField(blank=True, null=True)),
                ('catalog_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items', to='SalesManager.Storage')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='SalesManager.Item'),
        ),
    ]
