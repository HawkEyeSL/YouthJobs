from django.db import models
from django.contrib.auth.models import User
import MySQLdb

class Districts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.name)

class Applicants(models.Model):
    id = models.AutoField(primary_key=True)
    auth_id = models.ForeignKey(User)
    full_name = models.CharField(max_length=200)
    birth_year = models.IntegerField()
    birth_month = models.IntegerField()
    birth_day = models.IntegerField()
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=200)
    gender = models.BooleanField()
    district = models.ForeignKey(Districts)
    completed = models.BooleanField(default=False)
    updated = models.DateTimeField('date updated')
    created = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s' % (self.id, self.auth_id, self.full_name, 
            self.birth_year, self.birth_month, self.birth_day, self.address, 
            self.phone, self.gender, self.completed, self.updated, self.created)


class Companies(models.Model):
    id = models.AutoField(primary_key=True)
    auth_id = models.ForeignKey(User) 
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    company_reg_no = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=200)
    phone2 = models.CharField(max_length=200)
    district = models.ForeignKey(Districts) 
    type = models.IntegerField()
    postal_code = models.IntegerField()
    completed = models.BooleanField(default=False)
    updated = models.DateTimeField('date updated')
    created = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.id, self.auth_id, self.name, self.address, self.company_reg_no, 
            self.phone1, self.phone2, self.district, self.type, self.postal_code, self.completed, self.updated, self.created)

class User_verifications(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    company_id = models.ForeignKey(Companies)
    code = models.CharField(max_length=200)
    used = models.IntegerField()
    created = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.id, self.user_id, self.company_id, self.code, self.used, self.created)

class User_password_recover(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    company_id = models.ForeignKey(Companies)
    random_code = models.CharField(max_length=200)
    is_valid = models.IntegerField()
    updated = models.DateTimeField('date updated')
    created = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s %s %s %s %s %s' % (self.id, self.user_id, self.company_id, self.random_code, self.is_valid, self.updated, self.created)

