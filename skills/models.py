from django.db import models

class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return u'%s %s' % (self.id, self.name)

