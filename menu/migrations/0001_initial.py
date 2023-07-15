# Generated by Django 2.2 on 2023-07-13 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('numeroOrden', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('mesa', models.IntegerField()),
                ('mesero', models.IntegerField()),
                ('codigoEstado', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
            options={
                'db_table': 'orden',
            },
        ),
        migrations.CreateModel(
            name='OrdenProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('notas', models.CharField(blank=True, max_length=255)),
                ('orden', models.ForeignKey(db_column='numeroOrden', on_delete=django.db.models.deletion.CASCADE, to='menu.Orden')),
                ('producto', models.ForeignKey(db_column='numeroProducto', on_delete=django.db.models.deletion.CASCADE, to='administracion.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='productos',
            field=models.ManyToManyField(blank=True, through='menu.OrdenProducto', to='administracion.Producto'),
        ),
    ]
