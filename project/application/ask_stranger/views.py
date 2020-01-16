from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def get_pop_tags():
    pop_tags = list()
    for i in range(10):
        pop_tags.append({'name': 'tag ' + str(i)})
    return pop_tags


def get_best_users():
    best_users = list()
    for i in range(10):
        best_users.append({'name': 'best user ' + str(i)})
    return best_users

def validate_limit(limit):
    try:
        if limit > 1000:
            raise Exception("set default limit")
    except TypeError:
        limit = 10
    return limit


def validate_page(page):
    try:
        page = int(page)
        if page <= 0:
            raise Exception("set default page")
    except TypeError:
        page = 1
    return page


def paginate(query_set, page, limit=10):
    limit = validate_limit(limit)
    page = validate_page(page)
    paginator = Paginator(query_set, limit)
    return paginator.get_page(page), paginator


def index(request):
    page_num = request.GET.get('page')
    description = 'Новые вопросы'

    questions = []
    for i in range(50):
        questions.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'teeeeext' + str(i),
            'author': 'author' + str(i),
            'likes': i,
            'dislikes': i,
        })

    page_contents, paginator = paginate(questions, page_num)
    return render(request, 'ask_stranger/index.html',
                  {'page': page_contents,
                   'description': description,
                   'paginator': paginator,
                   'popular_tags': get_pop_tags(),
                   'best_users': get_best_users()})


def hot(request):
    page_num = request.GET.get('page')
    description = 'Лучшие вопросы'

    questions = []
    for i in range(50):
        questions.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'teeeeext' + str(i),
        })

    page_contents, paginator = paginate(questions, page_num)

    return render(request, 'ask_stranger/index.html',
                  {'page': page_contents,
                   'description': description,
                   'paginator': paginator,
                   'popular_tags': get_pop_tags(),
                   'best_users': get_best_users()})


def tagged(request, tag='default'):
    page_num = request.GET.get('page')
    descripsion = 'Вопросы по тэгу "' + tag + '"';

    questions = []
    for i in range(50):
        questions.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'teeeeext' + str(i),
        })

    page_contents, paginator = paginate(questions, page_num)

    return render(request, 'ask_stranger/index.html',
                  {'page': page_contents,
                   'description': descripsion,
                   'paginator': paginator,
                   'popular_tags': get_pop_tags(),
                   'best_users': get_best_users()})


def question(request, question_id):
    # question = get_object_or_404(Question, pk = question_id)
    # answers  = get_list_or_404(Answer, question_id = question_id)
    page_num = request.GET.get('page')

    question = {
        'title': 'title' + str(question_id),
        'id': 'id ' + str(question_id),
        'text': 'teeeeext' + str(question_id),
    }

    answer = []
    for i in range(50):
        answer.append({
            'user': 'user' + str(i),
            'text': 'answer' + str(i),
            'author': 'author' + str(i),
            'likes': i,
            'dislikes': i,
        })
    page_contents, paginator = paginate(answer, page_num)

    return render(request, 'ask_stranger/question.html',
                  {'page': page_contents,
                   'question': question,
                   'paginator': paginator,
                   'popular_tags': get_pop_tags(),
                   'best_users': get_best_users()})


def login(request):
    return render(request, 'ask_stranger/login.html',
                  {'popular_tags': get_pop_tags(),
                   'best_users': get_best_users()})


def signup(request):
    return render(request, 'ask_stranger/signup.html',
                  {'popular_tags': get_pop_tags(),
                   'best_users': get_best_users()})


def ask(request):
    return render(request, 'ask_stranger/ask.html',
                  {'popular_tags': get_pop_tags(),
                   'best_users': get_best_users()})
