# Generated by Django 3.1.6 on 2021-07-07 22:52

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telefono', models.CharField(blank=True, max_length=12, null=True)),
                ('cpp', models.IntegerField(blank=True, null=True)),
                ('calle', models.CharField(blank=True, max_length=50)),
                ('N_interior', models.CharField(blank=True, max_length=10)),
                ('N_exterior', models.CharField(blank=True, max_length=10)),
                ('colonia', models.CharField(blank=True, max_length=50)),
                ('municipio', models.CharField(blank=True, max_length=20)),
                ('estado', models.CharField(blank=True, max_length=20)),
                ('ciudad', models.CharField(blank=True, max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('descripcion', models.TextField(blank=True)),
                ('precio', models.IntegerField()),
                ('categoria', models.CharField(choices=[('SP', 'Sports'), ('CU', 'Cubrebocas'), ('SC', 'Scrunchies'), ('BA', 'Trajes de Baño'), ('CA', 'Mandiles'), ('TW', 'Twerk')], max_length=64)),
                ('pic0', models.CharField(max_length=256)),
                ('sexo', models.CharField(blank=True, choices=[('EL', 'Hombre'), ('ELLA', 'Mujer')], max_length=64)),
                ('n_pics', models.IntegerField()),
                ('pic1', models.CharField(blank=True, max_length=256)),
                ('pic2', models.CharField(blank=True, max_length=256)),
                ('pic3', models.CharField(blank=True, max_length=256)),
                ('pic4', models.CharField(blank=True, max_length=256)),
                ('color_disp', models.CharField(blank=True, max_length=256)),
                ('soldout', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(choices=[('PE', 'Pedido'), ('VE', 'Verificando Pago'), ('PR', 'En processo'), ('EN', 'Enviado'), ('RE', 'Recibido')], max_length=16)),
                ('fecha', models.DateTimeField(blank=True)),
                ('folio', models.IntegerField(blank=True)),
                ('cantidad', models.IntegerField()),
                ('talla', models.CharField(blank=True, max_length=64)),
                ('color', models.CharField(blank=True, max_length=64)),
                ('identifier', models.IntegerField(blank=True)),
                ('envio', models.CharField(blank=True, max_length=50)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_bougth', to='shop.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('talla', models.CharField(blank=True, max_length=64)),
                ('color', models.CharField(blank=True, max_length=64)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_watched', to='shop.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watcher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
