# Generated by Django 4.2 on 2023-04-10 14:27

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoalBonus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('contract', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('api_key', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('contract', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('bonuses_quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('blockchain', models.TextField()),
                ('private', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('ton_of_carbon_equivalent', models.IntegerField()),
                ('coal_bonuses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.coalbonus')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('buy', models.BooleanField(default=False)),
                ('sell', models.BooleanField(default=False)),
                ('create', models.BooleanField(default=False)),
                ('edit', models.BooleanField(default=False)),
                ('delete', models.BooleanField(default=False)),
                ('list', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomPermission',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.permission',),
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
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
                ('user_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('verified', models.BooleanField(default=False)),
                ('nit', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', related_query_name='custom_user', to='users.customgroup', verbose_name='groups')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.role')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_set', related_query_name='custom_user', to='users.custompermission', verbose_name='user permissions')),
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
            name='PurchaseOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('bonuses_quantity', models.IntegerField()),
                ('purchase_value', models.FloatField()),
                ('verified', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_orders', to='users.user')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.paymentmethod')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='developer_projects', to='users.user'),
        ),
        migrations.AddField(
            model_name='project',
            name='enterprise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enterprise_projects', to='users.user'),
        ),
        migrations.AddField(
            model_name='project',
            name='investor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investor_projects', to='users.user'),
        ),
        migrations.AddField(
            model_name='coalbonus',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coal_bonuses', to='users.user'),
        ),
    ]
