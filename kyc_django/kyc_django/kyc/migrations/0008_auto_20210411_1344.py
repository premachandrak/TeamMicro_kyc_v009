# Generated by Django 3.1.7 on 2021-04-11 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyc', '0007_auto_20210411_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc_infotemp',
            name='blue_flag_temp',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='kyc_infotemp',
            name='blue_flagadd_temp',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='kyc_infotemp',
            name='driv_exp_temp',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='kyc_infotemp',
            name='driv_lic_temp',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='kyc_infotemp',
            name='email_add_temp',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='kyc_infotemp',
            name='nationality_other_temp',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='kyc_infotemp',
            name='office_num_temp',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='kyc_infotemp',
            name='pass_exp_temp',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='kyc_infotemp',
            name='pass_no_temp',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='kyc_infotemp',
            name='red_flag_temp',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
