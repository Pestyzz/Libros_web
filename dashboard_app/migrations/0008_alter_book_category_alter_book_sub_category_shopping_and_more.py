# Generated by Django 5.0.6 on 2024-07-01 05:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0007_alter_book_category_alter_book_sub_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('1', 'Ficción'), ('2', 'No Ficción'), ('3', 'Aventura'), ('4', 'Ciencia Ficción'), ('5', 'Fantasía'), ('6', 'Misterio'), ('7', 'Thriller'), ('8', 'Romance'), ('9', 'Terror'), ('10', 'Biografía'), ('11', 'Autobiografía'), ('12', 'Historia'), ('13', 'Filosofía'), ('14', 'Ciencia'), ('15', 'Tecnología'), ('16', 'Matemáticas'), ('17', 'Salud'), ('18', 'Autoayuda'), ('19', 'Negocios'), ('20', 'Economía'), ('21', 'Política'), ('22', 'Sociología'), ('23', 'Psicología'), ('24', 'Educación'), ('25', 'Arte'), ('26', 'Música'), ('27', 'Teatro'), ('28', 'Cine'), ('29', 'Cocina'), ('30', 'Viajes'), ('31', 'Deportes'), ('32', 'Juegos'), ('33', 'Cómics'), ('34', 'Poesía'), ('35', 'Ensayo'), ('36', 'Crítica Literaria'), ('37', 'Religión'), ('38', 'Espiritualidad'), ('39', 'Juvenil'), ('40', 'Infantil'), ('41', 'Novela'), ('42', 'Suspenso')], max_length=20),
        ),
        migrations.AlterField(
            model_name='book',
            name='sub_category',
            field=models.CharField(blank=True, choices=[('1', 'Ficción'), ('2', 'No Ficción'), ('3', 'Aventura'), ('4', 'Ciencia Ficción'), ('5', 'Fantasía'), ('6', 'Misterio'), ('7', 'Thriller'), ('8', 'Romance'), ('9', 'Terror'), ('10', 'Biografía'), ('11', 'Autobiografía'), ('12', 'Historia'), ('13', 'Filosofía'), ('14', 'Ciencia'), ('15', 'Tecnología'), ('16', 'Matemáticas'), ('17', 'Salud'), ('18', 'Autoayuda'), ('19', 'Negocios'), ('20', 'Economía'), ('21', 'Política'), ('22', 'Sociología'), ('23', 'Psicología'), ('24', 'Educación'), ('25', 'Arte'), ('26', 'Música'), ('27', 'Teatro'), ('28', 'Cine'), ('29', 'Cocina'), ('30', 'Viajes'), ('31', 'Deportes'), ('32', 'Juegos'), ('33', 'Cómics'), ('34', 'Poesía'), ('35', 'Ensayo'), ('36', 'Crítica Literaria'), ('37', 'Religión'), ('38', 'Espiritualidad'), ('39', 'Juvenil'), ('40', 'Infantil'), ('41', 'Novela'), ('42', 'Suspenso')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=250)),
                ('card', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.IntegerField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('EP', 'EN PROCESO'), ('E', 'ENVIADO'), ('EN', 'ENTREGADO'), ('D', 'DEVUELTO'), ('C', 'CANCELADO')], default='EP', max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('shopping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='dashboard_app.shopping')),
            ],
        ),
    ]
