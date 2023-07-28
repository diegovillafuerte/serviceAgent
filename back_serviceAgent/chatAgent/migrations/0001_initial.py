# Generated by Django 4.2.3 on 2023-07-28 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companyAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('clientUser_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='None', max_length=100)),
                ('last_name', models.CharField(default='None', max_length=100)),
                ('email', models.EmailField(default='None', max_length=254)),
                ('phone_number', models.IntegerField(default=0)),
                ('company', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='companyAdmin.companyuser')),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('active', 'Active'), ('finished', 'Finished'), ('failed', 'Failed')], default='active', max_length=10)),
                ('clientUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatAgent.clientuser')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(choices=[('user', 'User'), ('agent', 'agent')], max_length=5)),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chatAgent.conversation')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.AddField(
            model_name='clientuser',
            name='current_conversation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chatAgent.conversation'),
        ),
    ]