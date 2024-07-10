import csv
import sys
from django.core.management.base import BaseCommand
from django.utils.text import slugify

class Command(BaseCommand):

    def handle(self, *args, **options):
        from phones.models import Phone
        self.stdout.write("Importing phones...")
        with open('phones.csv', 'r', newline='') as csvfile:
            phones_reader = csv.reader(csvfile, delimiter=';', quotechar=chr(10))
            phone = Phone()
            for cntr, row in enumerate(phones_reader):
                if cntr > 0:
                    phone.id = row[0]
                    phone.name = row[1]
                    phone.image = row[2]
                    phone.price = row[3]
                    phone.release_date = row[4]
                    phone.lte_exists = row[5]
                    phone.slug = slugify(row[1])
                    phone.save()
                    print(str(phone))
        self.stdout.write("Import completed successfully.")
cmd = Command()
cmd = cmd.handle()
