# Generated by Django 4.2.4 on 2023-08-23 01:13

import _socket
from django.db import migrations, models
import django_audit_fields.fields.hostname_modification_field


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_rando", "0003_alter_randomizationlist_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalrandomizationlist",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="historicalrandomizationlist",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="historicalrandomizationlist",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalrandomizationlist",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalregisteredgroup",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="historicalregisteredgroup",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="historicalregisteredgroup",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalregisteredgroup",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="randomizationlist",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="randomizationlist",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="randomizationlist",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="randomizationlist",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="registeredgroup",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="registeredgroup",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="registeredgroup",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="registeredgroup",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
    ]
