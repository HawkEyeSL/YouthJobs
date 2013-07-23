from django.db import models
from youthjob.models import Applicants

class Applicant_cv(models.Model):
    applicant_id = models.ForeignKey(Applicants)
    profile = models.TextField()
    education = models.TextField()
    projects = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    extra = models.TextField()
    recommend = models.TextField()

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s' % (self.applicant_id, self.profile, self.education, self.experience, self.skills, self.projects,
        	self.extra, self.recommend)