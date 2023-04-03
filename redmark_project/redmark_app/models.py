from django.db import models
from enum import Enum
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class Question(models.Model):
    __tablename__ = "questions"
    # This is the model for the questions table
    # This is the primary key for the questions table
    id = models.AutoField(primary_key=True)
    # This is the question column for the questions table
    question_text = models.TextField()
    # This is the relationship between the questions table and the options table
    answer = models.ManyToManyField('Answer', related_name='question_answers')
    options = models.ManyToManyField('Options', related_name='question')

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
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='quest_options')

    # This is the representation of the options table
    def __str__(self):
        # This returns the option
        return f"{self.a}, {self.b}, {self.c}, {self.d}, {self.e}"


class Is_answered(models.Model):
    __tablename__ = "is_answered"
    # This is the model for the is_answered table
    # This is the primary key for the is_answered table
    id = models.AutoField(primary_key=True)
    #  This is the user_id column for the is_answered table
    user_id = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    # This is the relationship between the is_answered table and the questions table
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE)

    # This is the representation of the is_answered table
    def __str__(self):
        # This returns the user_id
        return f"{self.user_id}, {self.question_id}"


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
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='question_options')

    # This is the representation of the answers table
    def __str__(self):
        # This returns the answer
        return f"{self.answer}"


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
