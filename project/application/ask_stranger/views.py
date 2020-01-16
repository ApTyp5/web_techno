from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def validate_limit(limit):
    try:
        if limit > 1000:
            raise Exception("set default limit")
    except TypeError:
        limit = 10
    return limit

def validate_page(page):
    try:
        if page <= 0:
            raise Exception("set default page")
    except TypeError:
        page = 1
    return page

def paginate(query_set, page, limit = 10):
    limit = validate_limit(limit)
    page = validate_page(page)
    paginator = Paginator(query_set, limit)
    return paginator.get_page(page)


def index(request, page=1):
    description = 'Новые вопросы'
    questions = []
    for i in range(50):
        questions.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'teeeeext' + str(i),
            'author': 'author' + str(i),
            'likes' : i,
            'dislikes': i,
        })
    questions = paginate(questions, page)
    return render(request, 'ask_stranger/index.html',
                  {'questions': questions, 'description': description})


def hot(request, page=1):
    description = 'Лучшие вопросы'
    questions = []
    for i in range(50):
        questions.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'teeeeext' + str(i),
        })

    questions = paginate(questions, page)

    return render(request, 'ask_stranger/index.html',
                  {'questions': questions, 'description': description})


def tagged(request, tag='default', page=1):
    descripsion = 'Вопросы по тэгу "' + tag + '"';
    questions = []
    for i in range(50):
        questions.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'teeeeext' + str(i),
        })

    questions = paginate(questions, page)

    return render(request, 'ask_stranger/index.html',
                  {'questions': questions, 'description': descripsion})


def question(request, question_id):
    # question = get_object_or_404(Question, pk = question_id)
    # answers  = get_list_or_404(Answer, question_id = question_id)

    question = {
        'title': 'title' + str(question_id),
        'id': 'id ' + str(question_id),
        'text': 'teeeeext' + str(question_id),
    }

    answers = []
    for i in range(10):
        answers.append({
            'user': 'user' + str(i),
            'text': 'answer' + str(i),
            'author': 'author' + str(i),
            'likes': i,
            'dislikes': i,
        })

    return render(request, 'ask_stranger/question.html', {'question': question, 'answers': answers})


def login(request):
    return render(request, 'ask_stranger/login.html', {})


def signup(request):
    return render(request, 'ask_stranger/signup.html', {})


def ask(request):
    return render(request, 'ask_stranger/ask.html', {})
