from django.db import models

class StudentsData(models.Model):
    roll_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    school_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    section_name = models.CharField(max_length=100)
    telugu_marks = models.IntegerField()
    hindi_marks = models.IntegerField()
    english_marks = models.IntegerField()
    maths_marks = models.IntegerField()
    science_marks = models.IntegerField()
    social_marks = models.IntegerField()


