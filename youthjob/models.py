from django.db import models
import MySQLdb

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.IntegerField()
    active = models.IntegerField()
    verified = models.IntegerField()
    updated = models.DateTimeField('date updated')
    created = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s' % (self.id, self.username, self.firstname, self.lastname, 
            self.email, self.phone, self.password, self.gender, self.active, self.verified, self.updated, self.created)

class Companies(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200) 
    company_reg_no = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=200)
    phone2 = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    district = models.IntegerField() 
    type = models.IntegerField()
    postal_code = models.IntegerField()
    active = models.IntegerField()
    verified = models.IntegerField()
    updated = models.DateTimeField('date updated')
    created = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.id, self.name, self.address, self.city, 
            self.company_reg_no, self.email, self.phone1, self.phone2, self.password, self.district, 
            self.type, self.postal_code, self.active, self.verified, self.updated, self.created)

class User_verifications(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users)
    company_id = models.ForeignKey(Companies)
    code = models.CharField(max_length=200)
    used = models.IntegerField()
    created = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.id, self.user_id, self.company_id, self.code, self.used, self.created)

class User_password_recover(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users)
    company_id = models.ForeignKey(Companies)
    random_code = models.CharField(max_length=200)
    is_valid = models.IntegerField()
    updated = models.DateTimeField('date updated')
    created = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s %s %s %s %s %s' % (self.id, self.user_id, self.company_id, self.random_code, self.is_valid, self.updated, self.created)
