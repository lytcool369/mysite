from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import board.models as boardModel


def index(request):
    page = request.GET['page']
    results = boardModel.fetchall(page)
    data = {'boardlist': results, 'page': page}

    return render(request, 'board/index.html', data)


def writeform(request):

    return render(request, 'board/writeform.html')


def write(request):
    title = request.POST['title']
    content = request.POST['content']
    boardModel.insert(title, content)

    return HttpResponseRedirect('/board?page=1')


def view(request):
    no = request.GET['no']
    result = boardModel.fetchone(no)
    boardModel.hit(no)
    data = {'view': result}

    return render(request, 'board/view.html', data)


def modifyform(request):
    no = request.GET['no']
    result = boardModel.fetchone(no)
    data = {'mf_view': result}

    return render(request, 'board/modifyform.html', data)


def modify(request):
    no = request.POST['no']
    title = request.POST['title']
    content = request.POST['content']

    boardModel.modify(title, content, no)
    result = boardModel.fetchone(no)
    data = {'view': result}

    return render(request, 'board/view.html', data)


def delete(request):
    no = request.GET['no']

    boardModel.delete(no)

    return HttpResponseRedirect('/board?page=1')