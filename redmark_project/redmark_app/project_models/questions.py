from django.db import models


# Create your models here.
class Question(models.Model):
    __tablename__ = "questions"
    # This is the model for the questions table
    # This is the primary key for the questions table
    id = models.AutoField(primary_key=True)
    # This is the question column for the questions table
    question = models.TextField()
    # This is the relationship between the questions table and the options table
    answer = models.ManyToManyField('Answer', related_name='q_to_ans')
    options = models.ManyToManyField('Options', related_name='question')

    # This is the representation of the questions table
    def __str__(self):
        # This returns the question
        return f"{self.question}"
