# Generated by Django 3.1.7 on 2021-03-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kyc_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('name_init', models.CharField(max_length=100)),
                ('id_type', models.CharField(max_length=50)),
                ('nics_no', models.CharField(max_length=50)),
                ('driv_lic', models.CharField(max_length=50)),
                ('pass_no', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('nationality_other', models.CharField(max_length=50)),
                ('house_no', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('mob_no', models.CharField(max_length=20)),
                ('office_num', models.CharField(max_length=20)),
                ('home', models.CharField(max_length=20)),
                ('email_add', models.CharField(max_length=50)),
                ('occu_state', models.CharField(max_length=50)),
            ],
        ),
    ]