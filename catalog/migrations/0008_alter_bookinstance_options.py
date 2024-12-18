# Generated by Django 5.1.2 on 2024-11-16 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'), ('can_view_all_borrowed_books', 'Can view all users borrowed'), ('add_author', 'Can add author'))},
        ),
    ]
