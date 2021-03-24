import pytest
import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "../../apidemocrud"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apidemocrud.settings")

# from django.conf import settings
# settings.configure()
import django  # noqa

django.setup()
