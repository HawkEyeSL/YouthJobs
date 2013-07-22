from django.db import models
from django.contrib.auth.models import User
from time import time
import MySQLdb

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

TYPE_CHOICES = (
    ('IT', 'IT'),
    ('BPO', 'BPO'),
)

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)

class Districts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.name)

class Applicants(models.Model):
    id = models.AutoField(primary_key=True)
    auth_id = models.ForeignKey(User)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    full_name = models.CharField(max_length=200)
    thumbnail = models.FileField(upload_to=get_upload_file_name)
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
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.id, self.auth_id, self.title, self.full_name, 
            self.thumbnail, self.birth_year, self.birth_month, self.birth_day, self.address, 
            self.phone, self.gender, self.district, self.completed, self.updated, self.created)


class Companies(models.Model):
    id = models.AutoField(primary_key=True)
    auth_id = models.ForeignKey(User) 
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    company_reg_no = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=200)
    phone2 = models.CharField(max_length=200)
    district = models.ForeignKey(Districts) 
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    postal_code = models.IntegerField()
    completed = models.BooleanField(default=False)
    updated = models.DateTimeField('date updated')
    created = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.id, self.auth_id, self.name, self.address, self.company_reg_no, 
            self.phone1, self.phone2, self.district, self.type, self.postal_code, self.completed, self.updated, self.created)

class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    applicant_id = models.ForeignKey(Applicants)
    from_date = models.CharField(max_length=200)
    to_date = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.id, self.applicant_id, self.from_date, self.to_date, self.company, self.description)

class Extra_Curriculum_Activity(models.Model):
    id = models.AutoField(primary_key=True)
    applicant_id = models.ForeignKey(Applicants)
    type = models.IntegerField()
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.id, self.applicant_id, self.type, self.description)

class Education(models.Model):
    id = models.AutoField(primary_key=True)
    applicant_id = models.ForeignKey(Applicants)
    year = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    result = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.id, self.applicant_id, self.from_date, self.to_date, self.company, self.description)

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

