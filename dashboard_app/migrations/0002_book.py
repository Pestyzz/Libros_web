# Generated by Django 5.0.6 on 2024-06-07 05:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('isbn', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1000000000000), django.core.validators.MaxValueValidator(9999999999999)])),
                ('book_name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=15)),
                ('languages', models.CharField(choices=[('EN', 'Inglés'), ('ES', 'Español')], max_length=20)),
                ('description', models.TextField(max_length=1500)),
                ('image', models.ImageField(upload_to='books')),
                ('category', models.CharField(choices=[('13', 'Filosofía'), ('30', 'Viajes'), ('17', 'Salud'), ('7', 'Thriller'), ('5', 'Fantasía'), ('36 Literaria', 'Crítica Literaria'), ('12', 'Historia'), ('10', 'Biografía'), ('21', 'Política'), ('26', 'Música'), ('14', 'Ciencia'), ('37', 'Religión'), ('32', 'Juegos'), ('22', 'Sociología'), ('29', 'Cocina'), ('4', 'Ciencia Ficción'), ('1', 'Ficción'), ('19', 'Negocios'), ('23', 'Psicología'), ('34', 'Poesía'), ('35', 'Ensayo'), ('6', 'Misterio'), ('25', 'Arte'), ('39', 'Juvenil'), ('33', 'Cómics'), ('24', 'Educación'), ('8', 'Romance'), ('28', 'Cine'), ('2', 'No Ficción'), ('40', 'Infantil'), ('3', 'Aventura'), ('38', 'Espiritualidad'), ('27', 'Teatro'), ('20', 'Economía'), ('31', 'Deportes'), ('11', 'Autobiografía'), ('15', 'Tecnología'), ('18', 'Autoayuda'), ('9', 'Terror'), ('16', 'Matemáticas')], max_length=20)),
                ('sub_category', models.CharField(blank=True, choices=[('13', 'Filosofía'), ('30', 'Viajes'), ('17', 'Salud'), ('7', 'Thriller'), ('5', 'Fantasía'), ('36 Literaria', 'Crítica Literaria'), ('12', 'Historia'), ('10', 'Biografía'), ('21', 'Política'), ('26', 'Música'), ('14', 'Ciencia'), ('37', 'Religión'), ('32', 'Juegos'), ('22', 'Sociología'), ('29', 'Cocina'), ('4', 'Ciencia Ficción'), ('1', 'Ficción'), ('19', 'Negocios'), ('23', 'Psicología'), ('34', 'Poesía'), ('35', 'Ensayo'), ('6', 'Misterio'), ('25', 'Arte'), ('39', 'Juvenil'), ('33', 'Cómics'), ('24', 'Educación'), ('8', 'Romance'), ('28', 'Cine'), ('2', 'No Ficción'), ('40', 'Infantil'), ('3', 'Aventura'), ('38', 'Espiritualidad'), ('27', 'Teatro'), ('20', 'Economía'), ('31', 'Deportes'), ('11', 'Autobiografía'), ('15', 'Tecnología'), ('18', 'Autoayuda'), ('9', 'Terror'), ('16', 'Matemáticas')], max_length=20, null=True)),
                ('is_new', models.BooleanField(default=True)),
                ('on_sale', models.BooleanField(default=False)),
                ('publish', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
