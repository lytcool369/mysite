from django.shortcuts import render
import board.models as boardModel


def index(request):
    results = boardModel.fetchall()
    data = {'boardlist': results}

    return render(request, 'board/index.html', data)


def view(request):
    return render(request, 'board/view.html')


def modify(request):
    return render(request, 'board/modify.html')


def write(request):
    return render(request, 'board/write.html')