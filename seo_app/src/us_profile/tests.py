from django.test import TestCase
import requests


r = requests.get('https://avito.ru/').text

print(r)