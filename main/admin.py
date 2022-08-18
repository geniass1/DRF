from django.contrib import admin

from .models import Person, Company, Employer, Offices, Skills, Level, Languages

admin.site.register([Person, Company, Employer, Offices, Skills, Level, Languages])