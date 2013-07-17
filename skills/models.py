from django.db import models

class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return u'%s %s' % (self.id, self.name)

class Tree(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(Skill,related_name='tree_child')
    child = models.ForeignKey(Skill,related_name='tree_parent')
    relation = models.CharField(max_length=200)
    strength = models.IntegerField()

    def __str__(self):
        return u'%s %s %s %s' % (self.id, self.parent, self.child, 
            self.relation, self.strength)
