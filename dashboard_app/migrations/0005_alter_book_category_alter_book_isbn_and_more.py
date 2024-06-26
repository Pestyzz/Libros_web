# Generated by Django 5.0.6 on 2024-06-10 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0004_alter_book_category_alter_book_languages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('4', 'Ciencia Ficción'), ('6', 'Misterio'), ('30', 'Viajes'), ('20', 'Economía'), ('3', 'Aventura'), ('18', 'Autoayuda'), ('32', 'Juegos'), ('23', 'Psicología'), ('29', 'Cocina'), ('34', 'Poesía'), ('28', 'Cine'), ('7', 'Thriller'), ('8', 'Romance'), ('27', 'Teatro'), ('1', 'Ficción'), ('39', 'Juvenil'), ('21', 'Política'), ('2', 'No Ficción'), ('19', 'Negocios'), ('12', 'Historia'), ('14', 'Ciencia'), ('40', 'Infantil'), ('35', 'Ensayo'), ('10', 'Biografía'), ('16', 'Matemáticas'), ('22', 'Sociología'), ('31', 'Deportes'), ('15', 'Tecnología'), ('25', 'Arte'), ('38', 'Espiritualidad'), ('13', 'Filosofía'), ('36', 'Crítica Literaria'), ('24', 'Educación'), ('17', 'Salud'), ('33', 'Cómics'), ('37', 'Religión'), ('26', 'Música'), ('5', 'Fantasía'), ('9', 'Terror'), ('11', 'Autobiografía')], max_length=20),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1000000000000), django.core.validators.MaxValueValidator(9999999999999)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='languages',
            field=models.CharField(choices=[('EN', 'Inglés'), ('ES', 'Español')], max_length=20),
        ),
        migrations.AlterField(
            model_name='book',
            name='sub_category',
            field=models.CharField(blank=True, choices=[('4', 'Ciencia Ficción'), ('6', 'Misterio'), ('30', 'Viajes'), ('20', 'Economía'), ('3', 'Aventura'), ('18', 'Autoayuda'), ('32', 'Juegos'), ('23', 'Psicología'), ('29', 'Cocina'), ('34', 'Poesía'), ('28', 'Cine'), ('7', 'Thriller'), ('8', 'Romance'), ('27', 'Teatro'), ('1', 'Ficción'), ('39', 'Juvenil'), ('21', 'Política'), ('2', 'No Ficción'), ('19', 'Negocios'), ('12', 'Historia'), ('14', 'Ciencia'), ('40', 'Infantil'), ('35', 'Ensayo'), ('10', 'Biografía'), ('16', 'Matemáticas'), ('22', 'Sociología'), ('31', 'Deportes'), ('15', 'Tecnología'), ('25', 'Arte'), ('38', 'Espiritualidad'), ('13', 'Filosofía'), ('36', 'Crítica Literaria'), ('24', 'Educación'), ('17', 'Salud'), ('33', 'Cómics'), ('37', 'Religión'), ('26', 'Música'), ('5', 'Fantasía'), ('9', 'Terror'), ('11', 'Autobiografía')], max_length=20, null=True),
        ),
    ]
