from django.db import migrations


def test_function():
    print("I am just another RunPython Migration, ready to be squashed!")


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0004_squashed'),
    ]

    operations = [
        migrations.RunPython(test_function, elidable=False),
    ]
