from django.db import models
from enum import Enum


# define an enum for the answer choices
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
    # This is the is_correct column for the answers table
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE)

    # This is the representation of the answers table
    def __str__(self):
        # This returns the answer
        return f"{self.answer}"
