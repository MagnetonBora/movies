import os

from django.contrib.auth.models import User
from django.db import IntegrityError


username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
try:
    superuser = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    superuser.save()
except IntegrityError:
    print(f"Super User with username {username} is already present")
except Exception as e:
    print(e)
