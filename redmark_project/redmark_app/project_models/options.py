from django.db import models


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
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE)

    # This is the representation of the options table
    def __str__(self):
        # This returns the option
        return f"{self.a}, {self.b}, {self.c}, {self.d}, {self.e}"
