from django.db import models
from enum import Enum
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    __tablename__ = "questions"
    # This is the model for the questions table
    # This is the primary key for the questions table
    id = models.AutoField(primary_key=True)
    # This is the question column for the questions table
    question_text = models.TextField()
    # This is the relationship between the questions table and the answer table
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, related_name='question_answer', null=True, blank=True)

    # This is the representation of the questions table
    def __str__(self):
        # This returns the question
        return f"{self.question_text}"


class Options(models.Model):
    __tablename__ = "options"
    # This is the model for the options table
    # This is the primary key for the options table
    id = models.AutoField(primary_key=True)
    # This is the first option column for the options table
    a = models.TextField()
    # This is the second option column for the options table
    b = models.TextField()
    # This is the third option column for the options table
    c = models.TextField()
    # This is the fourth option column for the options table
    d = models.TextField()
    # This is the fifth option column for the options table
    e = models.TextField()
    # This is the relationship between the options table and the questions table
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='quest_options', null=True)

    # This is the representation of the options table
    def __str__(self):
        # This returns the option
        return f"{self.a}, {self.b}, {self.c}, {self.d}, {self.e}, {self.question}"


class Is_answered(models.Model):
    __tablename__ = "is_answered"
    # This is the model for the is_answered table
    # This is the primary key for the is_answered table
    id = models.AutoField(primary_key=True)
    #  This is the user_id column for the is_answered table
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    # This is the relationship between the is_answered table and the questions table
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    # This is the representation of the is_answered table
    def __str__(self):
        # This returns the user_id
        return f"{self.user}, {self.question}"


class Answer_enum(Enum):
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'
    E = 'e'


class Answer(models.Model):
    __tablename__ = "answers"
    # This is the model for the answers table
    # This is the primary key for the answers table
    id = models.AutoField(primary_key=True)
    # This is the answer column for the answers table
    answer = models.CharField(max_length=1,
                              choices=[(tag, tag.value) for tag in Answer_enum])
    # This is the relationship between the answers table and the questions table
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')

    # This is the representation of the answers table
    def __str__(self):
        # This returns the answer
        return f"{self.answer}"


class UserProfile(models.Model):
    __tablename__ = 'userprofile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)
    taken = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
