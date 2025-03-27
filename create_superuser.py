import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rmhs_dashboard.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='rmhs').exists():
    User.objects.create_superuser('rmhs', 'rmhs@example.com', 'nmdcrmhs')
    print("Superuser created: rmhs/nmdcrmhs")
else:
    print("Superuser already exists")
