from django.db import models
from time import time
import MySQLdb
from skills.models import Skill
from django.contrib.auth.models import User
from youthjob.models import Districts, Companies, Applicants
# Create your models here.

class Vacancy(models.Model):
    id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Companies)
    name = models.CharField(max_length=200)
    description = models.TextField()
    district = models.ForeignKey(Districts)
    
    experience = models.IntegerField() #values save in number of months, one year means 12 month
    
    VACANCY_TYPES = (
        ('1', 'IT'),
        ('2', 'BPO'),
    )
    vacancy_type = models.IntegerField(choices=VACANCY_TYPES)

    SALARY_RANGES = (
        ('1', '0 - 20,000'),
        ('2', '21,000 - 30,000'),
        ('3', '31,000 - 50,000'),
        ('4', '51,000 - 75,000'),
        ('5', '76,000 - 100,000'),
        ('6', '101,000 - 150,000'),
        ('7', '151,000 - 200,000'),
        ('8', 'above 200,000  '),
    )
    salary_ranges = models.IntegerField(choices=SALARY_RANGES)
    
    updated = models.DateTimeField('date updated')
    created = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s' % (self.id, self.company_id, 
            self.name, self.description, self.district, self.vacancy_type, 
            self.salary_ranges, self.updated, self.created)
    
class User_skills(models.Model):
    user_id = models.ForeignKey(Applicants)
    skill_id = models.ForeignKey(Skill)
    
    def __unicode__(self):
        return u'%s %s' % (self.user_id, self.skill_id)
    
class Vacancy_skills(models.Model):
    vacancy_id = models.ForeignKey(Vacancy)
    skill_id = models.ForeignKey(Skill)

    def __unicode__(self):
        return u'%s %s' % (self.vacancy_id, self.skill_id)

class Vacancy_personality(models.Model):
    vacancy_id = models.ForeignKey(Vacancy)
    personality_id = models.IntegerField()

    def __unicode__(self):
        return u'%s %s' % (self.vacancy_id, self.personality_id)

class Vacancy_applicants(models.Model):
    vacancy_id = models.ForeignKey(Vacancy)
    applicant_id = models.ForeignKey(Applicants)

    def __unicode__(self):
        return u'%s %s' % (self.vacancy_id, self.applicant_id)
