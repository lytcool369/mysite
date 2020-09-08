from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import board.models as boardModel


def index(request):
    results = boardModel.fetchall()
    data = {'boardlist': results}

    return render(request, 'board/index.html', data)


def view(request):
    no = request.GET['no']
    result = boardModel.fetchone(no)
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


def write(request):
    return render(request, 'board/write.html')