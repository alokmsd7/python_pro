

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='points',
            field=models.IntegerField(default=1),
        ),
    ]
