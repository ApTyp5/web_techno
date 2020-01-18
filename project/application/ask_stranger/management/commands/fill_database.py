from django.core.management.base import BaseCommand, CommandError
from ask_stranger.models import Tag, User, Question, Answer, QuestionLike, AnswerLike
from faker import Faker
from random import randint

user_num = 10001
question_per_user = 10  # question_num = 100 010
answer_per_user = 100  # answer_num = 1 000 010
tag_num = 10001
tags_per_question = 5
qlikes_per_user = 100  # question_likes_num = 1 000 010
alikes_per_user = 100  # anser_likes_num = 1 000 010

en_fake = Faker()
ru_fake = Faker('ru_RU')


def create_tags(tag_num):
    pref = 1

    for i in range(tag_num):
        tag = Tag(name=en_fake.job() + str(pref))
        tag.save()
        pref += 1


def create_users(user_num):
    pref = 1
    for i in range(user_num):
        user = User.objects.create_user(ru_fake.user_name() + str(pref), ru_fake.email(), ru_fake.password())
        user.save()
        pref += 1


def add_questions(question_per_user):
    max_tag_id = len(Tag.objects.all())

    for user in User.objects.all():
        for i in range(question_per_user):
            question = Question(ru_fake.job(), ru_fake.text(),
                                ru_fake.date_time_this_century(before_now=True, after_now=False),
                                user)
            question.save()
            for j in range(tags_per_question):
                tag = Tag.objects.get(pk=randint(1, max_tag_id))
                print("tag name",tag.name)
                question.tags.add(tag)


def add_answers(answer_per_user):
    max_question_id = len(Question.objects.all())

    for user in User.objects.all():
        for i in range(answer_per_user):
            q = Question.objects.get(pk=randint(1, max_question_id))
            a = Answer(ru_fake.text(), ru_fake.date_time_between_dates(datetime_start=q.creation_datetime),
                       q, user)
            a.save()


def find_unliked_not_owners_question(user):
    max_question_id = len(Question.objects.all())
    liked_questions = user.questionlike_set.all()
    asked_questions = user.question_set.all()

    while True:
        q = Question.objects.get(pk=randint(1, max_question_id))
        if q in asked_questions:
            continue
        if q in liked_questions:
            continue
        return q


def add_qlikes(qlikes_per_user):
    for user in User.objects.all():
        for i in range(qlikes_per_user):
            q = find_unliked_not_owners_question(user)
            rate = 1 if randint(0, 1) == 1 else -1

            like = QuestionLike(rate, ru_fake.date_time_between_dates(datetime_start=q.creation_datetime),
                                user, q)
            like.save()


def find_unliked_not_owners_answer(user):
    max_answer_id = len(Answer.objects.all())
    liked_answers = user.answerlike_set.all()
    written_answers = user.answer_set.all()

    while True:
        q = Answer.objects.get(pk=randint(1, max_answer_id))
        if q in written_answers:
            continue
        if q in liked_answers:
            continue
        return q


def add_alikes(alikes_per_user):
    for user in User.objects.all():
        for i in range(alikes_per_user):
            q = find_unliked_not_owners_answer(user)
            rate = 1 if randint(0, 1) == 1 else -1

            like = AnswerLike(rate, ru_fake.date_time_between_dates(datetime_start=q.creation_datetime),
                              user, q)
            like.save()


class Command(BaseCommand):
    help = 'fill database command'

    def handle(self, *args, **options):
        # create_tags(tag_num)
        print(1)
        # create_users(user_num)
        print(2)
        add_questions(question_per_user)
        print(3)
        add_answers(answer_per_user)
        print(4)
        add_qlikes(qlikes_per_user)
        print(5)
        add_alikes(alikes_per_user)
        print(6)
