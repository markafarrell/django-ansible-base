# Generated by Django 4.2.6 on 2024-08-05 16:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0013_alter_manageduser_managers_alter_user_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoExtraUUIDModel',
            fields=[
                ('uuidmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='test_app.uuidmodel')),
                ('extra_id', models.UUIDField(default=uuid.uuid4)),
            ],
            bases=('test_app.uuidmodel',),
        ),
        migrations.CreateModel(
            name='ManualExtraUUIDModel',
            fields=[
                ('uuidmodel_ptr', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='+', serialize=False, to='test_app.uuidmodel')),
                ('extra_id', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraExtraUUIDModel',
            fields=[
                ('extra_uuid', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='+', serialize=False, to='test_app.manualextrauuidmodel')),
                ('third_id', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
    ]