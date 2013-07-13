from django.db import models
from time import time
import MySQLdb
from skills.models import Skill
from django.contrib.auth.models import User
from youthjob.models import Districts
from companies.models import Companies

# Create your models here.

class Vacancies(models.Model):
    id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Companies)
    name = models.CharField(max_length=200)
    description = models.TextField()
    district = models.ForeignKey(Districts)
    
    experience = models.IntegerField() #values save in number of months, one year means 12 month
    personality = models.IntegerField() #for now it is a value between 0 - 100
    
    VACANCY_TYPES = (
        ('a', 'IT'),
        ('b', 'BPO'),
    )
    vacancy_type = models.CharField(max_length=1, choices=VACANCY_TYPES)

    SALARY_RANGES = (
        ('a', '0 - 20,000'),
        ('b', '21,000 - 30,000'),
        ('c', '31,000 - 50,000'),
        ('d', '51,000 - 75,000'),
        ('e', '76,000 - 100,000'),
        ('f', '101,000 - 150,000'),
        ('g', '151,000 - 200,000'),
        ('f', 'above 200,000  '),
    )
    salari_ranger = models.CharField(max_length=1, choices=SALARY_RANGES)
    
    updated = models.DateTimeField('date updated')
    created = models.DateTimeField('date published')
    
class User_skils(models.Model):
    user_id = models.ForeignKey(User) 
    skill_id = models.ForeignKey(Skill)
    
class Vacancy_skills(models.Model):
    vacancy_id = models.ForeignKey(Vacancies)
    skill_id = models.ForeignKey(Skil)