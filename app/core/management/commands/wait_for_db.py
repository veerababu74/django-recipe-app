# django command to wait for databse to be avilable
import time
from psycopg2 import OperationalError as Psycopgoperror
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """django command to wait for database"""

    def handle(self, *args, **options):
        self.stdout.write("waiting for databse...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopgoperror, OperationalError):
                self.stdout.write("database unavilable , waiting 1 second ...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("database avilable"))
