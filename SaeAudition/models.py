from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from register.models import Profile
# Create your models here.
def validate_image_size(value):
    limit = 1 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 1 MiB.')

def images(instance, filename):
    return 'pics/{filename}'.format(filename=filename)

class Question(models.Model):
    ques_round = models.IntegerField(default=1, primary_key=True)
    types = [
        ('T', 'TEXT'),
        ('I', 'IMAGE'),
        ('M','MCQ')
    ]
    question_type = models.CharField(max_length=1, choices=types,default='T')
    question_text = models.CharField(max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to='images', validators=[validate_image_size])

    def __str__(self):
        return str(self.ques_round)

class Answer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,related_name='answer',on_delete=models.CASCADE)
    question = models.ForeignKey(Question,related_name='allanswer',on_delete=models.CASCADE)
    answer_text = models.TextField()

    class Meta:
        ordering = ['question']

    def __str__(self):
         return "{} : {}".format(self.question.ques_round,self.profile.first_name+' '+self.profile.last_name)
