from django.contrib import admin
from .models import Answer, Options, Question, Is_answered, UserProfile


# Register your models here.
admin.site.register(Answer)
admin.site.register(Options)
admin.site.register(Question)
admin.site.register(Is_answered)
admin.site.register(UserProfile)
