from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import board.models as boardModel


def index(request):
    page = int(request.GET['page'])

    results_list = boardModel.fetchall(page)
    results_paging = boardModel.paging(page)
    paging = results_paging['paging']
    pcontrol = results_paging['pcontrol']
    data = {'boardlist': results_list, 'paging': paging, 'page': page, 'pcontrol': pcontrol}

    return render(request, 'board/index.html', data)


def view(request):
    page = request.GET['page']
    board_no = request.GET['no']

    result = boardModel.fetchone(board_no)
    boardModel.hit(board_no)
    data = {'view': result, 'page': page}

    return render(request, 'board/view.html', data)


def writeform(request):

    return render(request, 'board/writeform.html')


def write(request):
    user_no = request.session['authuser']['no']
    title = request.POST['title']
    content = request.POST['content']

    boardModel.insert_write(title, content, user_no)

    return HttpResponseRedirect('/board?page=1')


def replayform(request):
    board_no = request.GET['no']
    page = request.GET['page']
    data = {'board_no': board_no, 'page': page}

    return render(request, 'board/replayform.html', data)


def replay(request):
    user_no = request.session['authuser']['no']
    board_no = request.POST['board_no']
    title = request.POST['title']
    content = request.POST['content']
    page = request.POST['page']

    board = boardModel.fetchone(board_no)
    boardModel.replay(board_no, title, content, board, user_no)

    return HttpResponseRedirect(f'/board?page={page}')


def modifyform(request):
    board_no = request.GET['no']
    page = request.GET['page']
    result = boardModel.fetchone(board_no)
    data = {'mf_view': result, 'page': page}

    return render(request, 'board/modifyform.html', data)


def modify(request):
    board_no = request.POST['no']
    title = request.POST['title']
    content = request.POST['content']

    boardModel.modify(title, content, board_no)
    result = boardModel.fetchone(board_no)
    data = {'view': result}

    return render(request, 'board/view.html', data)


def delete(request):
    page = int(request.GET['page'])
    board_cnt = int(request.GET['board_cnt'])
    board_no = request.GET['no']

    board = boardModel.fetchone(board_no)
    boardModel.delete(board_no, board)

    if board_cnt == 1 and page > 1:
        return HttpResponseRedirect(f'/board?page={page - 1}')
    else:
        return HttpResponseRedirect(f'/board?page={page}')