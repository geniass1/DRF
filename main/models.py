from django.db import models


class BaseContent(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Offices(BaseContent):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Company(BaseContent):
    name = models.CharField(max_length=100)
    offices = models.ManyToManyField('Offices')
    employees = models.ManyToManyField('Employer', blank=True)
    cooperation = models.ManyToManyField('Company', blank=True)

    def __str__(self):
        return self.name

    @property
    def num_office(self):
        return self.offices.count()

    @property
    def num_employees(self):
        return self.employees.count()


class Person(BaseContent):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, default=None)
    age = models.IntegerField()
    languages = models.ManyToManyField('Languages', blank=True)
    skills = models.ManyToManyField('Skills', blank=True)

    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length=100)
    level = models.ForeignKey('Level', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(max_length=100)
    level = models.ForeignKey('Level', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employer(BaseContent):
    job_title = models.CharField(max_length=100)
    person_id = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.job_title
