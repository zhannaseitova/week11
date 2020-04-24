from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, default='company_name')
    description = models.TextField(default='')
    city = models.CharField(max_length=50, default='company_city')
    address = models.TextField(default='company_address')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=100, default='vacancy_name')
    description = models.TextField(default='')
    salary = models.FloatField(default=5000)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company_id
        }