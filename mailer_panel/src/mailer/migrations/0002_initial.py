from django.db import migrations
from mailer.mail_template import welcome, like, personal_selection, mass, private

from datetime import datetime

date_ = datetime.now()


class Migration(migrations.Migration):
    dependencies = [
        ('mailer', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql=f"""INSERT INTO email_templates (id, name, html_text,created_at, updated_at) VALUES 
                    (1, 'welcome', '{welcome}', '{date_}', '{date_}'),
                    (2, 'like', '{like}', '{date_}', '{date_}'),
                    (3, 'personal_selection', '{personal_selection}', '{date_}', '{date_}'),
                    (4, 'mass', '{mass}', '{date_}', '{date_}'),
                    (5, 'private', '{private}', '{date_}', '{date_}');"""
        ),
    ]
