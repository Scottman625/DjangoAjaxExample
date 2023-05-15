from django.test import TestCase
import csv
import os
from .models import City, County
# Create your tests here.
def importCityCounty():
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'county.csv')

    file = open(file_path)
    reader = csv.reader(file, delimiter=',')
    for index, row in enumerate(reader):
        if index != 0:
            if City.objects.filter(name=row[0]).count()==0:
                city = City()
                city.name = row[0]
                city.newebpay_cityname = row[6]
                city.save()
            else:
                city = City.objects.get(name=row[0])

            county_name = row[2].replace(row[0],'')
            county = County()
            county.city = city
            county.name = county_name
            county.save()
            print(city.name + " " + county.name)