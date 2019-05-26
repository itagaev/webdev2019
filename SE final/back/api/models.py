from django.db import models
import datetime

class CompetitionManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class Competition(models.Model): 
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(datetime.datetime.now())
    due_on = models.DateTimeField(auto_now_add=True)
    requirements = models.CharField(max_length=500)
    field = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return '{} :{}'.format(self.id,self.name,self.city,self.created_at,self.due_on,self.requirements,self.field,self.email)
    def to_json(self):
        return {
            'id':self.id,
            'name': self.name,
            'city': self.city,
            'created at': self.created_at,
            'due on': self.due_on,
            'requirements': self.requirements,
            'fields': self.field,
            'e-mail': self.email
        }

class Members(models.Model):
    membername = models.CharField(max_length=50)
    memberlocation = models.CharField(max_length=50)
    memberemail = models.EmailField()
    comps = models.ForeignKey(Competition, on_delete= models.CASCADE)
    def __str__(self):
        return '{} :{}'.format(self.membername,self.memberlocation,self.memberemail)
    def to_json(self):
        return {
            'Member name':self.membername,
            'Member location':self.memberlocation,
            'Member email':self.memberemail,
            'Competition':self.comps.to_json()
    }