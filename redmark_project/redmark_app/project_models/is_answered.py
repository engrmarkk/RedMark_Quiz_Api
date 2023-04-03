from django.db import models


class Is_answered(models.Model):
    __tablename__ = "is_answered"
    # This is the model for the is_answered table
    # This is the primary key for the is_answered table
    id = models.AutoField(primary_key=True)
    #  This is the user_id column for the is_answered table
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    # This is the relationship between the is_answered table and the questions table
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE)

    # This is the representation of the is_answered table
    def __str__(self):
        # This returns the user_id
        return f"{self.user_id}, {self.question_id}"
