from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Profile(models.Model):
    status = [
        (1,'NOT_EVALUATED'),
        (2,'EVALUATED'),
        (3,'ELIMINATED'),
    ]

    user = models.OneToOneField(User,on_delete=CASCADE,default=None,primary_key=True)
    first_name=models.CharField(max_length=120,null=False,default='a')
    last_name=models.CharField(max_length=120,null=False,default='a')
    curr_round = models.IntegerField(default=1)
    current_status = models.IntegerField(choices=status,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    member= models.BooleanField(default=False)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name



