from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def base(request):
    return render(request, 'ask_stranger/base.html', {})

def paginate(objects, page, objects_on_page = 10):
    paginator = Paginator(objects, objects_on_page)
    return paginator.get_page(page)


def index(request, page = 1):
    questions = []
    for i in range(50):
        questions.append({
            'title': 'title ' + str(i),
            'id'  : i,
            'text': 'teeeeext' + str(i),
    })

    questions = paginate(questions, page)

    return render(request, 'ask_stranger/index.html', {'questions':questions})

def hot(request, page = 1):
    for i in range(50):
        questions.append({
            'title': 'title ' + str(i),
            'id'  : i,
            'text': 'teeeeext' + str(i),
    })

    objects = paginate(objects, page)


    return render(request, 'ask_stranger/hot.html', {'questions':questions})


def tagged(request, tag = 'def', page = 1):
    for i in range(50):
        questions.append({
            'title': 'title ' + str(i),
            'id'  : i,
            'text': 'teeeeext' + str(i),
    })

    objects = paginate(objects, page)

    return render(request, 'ask_stranger/tagged.html', {'questions':questions})


def question(request, question_id):
    # question = get_object_or_404(Question, pk = question_id)
    # answers  = get_list_or_404(Answer, question_id = question_id)

    question = {
            'title': 'title' + str(question_id),
            'id'  : 'id ' + str(question_id),
            'text': 'teeeeext' + str(question_id),
    }

    answers = []
    for i in range(10):
        answers.append({
            'user': 'user' + str(i),
            'text': 'answer' + str(i),
        })

    return render(request, 'ask_stranger/question.html', {'question':question,'answers': answers})

def login(request):
    return render(request, 'ask_stranger/login.html', {})

def signup(request):
    return render(request, 'ask_stranger/signup.html', {})

def ask(request):
    return render(request, 'ask_stranger/ask.html', {})
