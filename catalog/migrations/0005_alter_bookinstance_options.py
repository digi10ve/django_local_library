# Generated by Django 5.1.2 on 2024-11-14 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'), ('can_view_all_borrowed_books', 'Can view all users borroed'))},
        ),
    ]