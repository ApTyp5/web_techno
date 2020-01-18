from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Model Managers

class QuestionManager(models.Manager):
    def new_questions(self):
        return self.all().order_by('-creation_datetime')

    def hot_questions(self):
        return self.all().order_by('-rating')

    def tagged_questions(self, tname):
        return Tag.objects.get(name=tname).questions.all()


# class AnswerManager(models.Manager):


# Models
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Question(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(null=False)
    creation_datetime = models.DateTimeField(default=datetime.now)
    rating = models.IntegerField(default=0)

    author = models.ForeignKey(User, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)

    objects = QuestionManager()

    def __init__(self, title, content, creation_datetime, author, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.content = content
        self.creation_datetime = creation_datetime
        self.author = author

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-creation_datetime']


class Answer(models.Model):
    content = models.TextField(null=False)
    creation_datetime = models.DateTimeField(default=datetime.now)
    correct = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)

    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __init__(self, content, creation_datetime, question, author, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = content
        self.creation_datetime = creation_datetime
        self.question = question
        self.author = author

    class Meta:
        ordering = ['-creation_datetime']


#   objects = AnswerManager()


class Profile(models.Model):
    registration_datetime = models.DateTimeField(default=datetime.now)
    avatar = models.FilePathField()

    user = models.OneToOneField(User, on_delete=models.PROTECT)


class QuestionLike(models.Model):
    rating = models.IntegerField(default=0)
    creation_datetime = models.DateTimeField(default=datetime.now)

    author = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)

    def __init__(self, rating, creation_datetime, author, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rating = rating
        self.creation_datetime = creation_datetime
        self.author = author
        self.question = question
        question.rating += rating
        question.save()

    class Meta:
        unique_together = ['author', 'question']


class AnswerLike(models.Model):
    rating = models.IntegerField(default=0)
    creation_datetime = models.DateTimeField(default=datetime.now)

    author = models.ForeignKey(User, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.PROTECT)

    def __init__(self, rating, creation_datetime, author, answer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rating = rating
        self.creation_datetime = creation_datetime
        self.author = author
        self.answer = answer
        answer.rating += rating
        answer.save()

    class Meta:
        unique_together = ['author', 'answer']
