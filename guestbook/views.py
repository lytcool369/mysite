from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import guestbook.models as guestbookModel


def index(request):
    results = guestbookModel.list()
    data = {'guestlist': results}
    return render(request, 'guestbook/index.html', data)


def insert(request):
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['message']

    guestbookModel.insert(name, password, message)

    return HttpResponseRedirect('/guestbook')


def deleteform(request):
    data = {'no': request.GET['no']}
    return render(request, 'guestbook/deleteform.html', data)


def delete(request):
    no = request.POST['no']
    password = request.POST['password']

    result = guestbookModel.delete(no, password)
    print(result)

    if result == 0:
        return HttpResponseRedirect('/guestbook')
    elif result == -1:
        return HttpResponse('비밀번호가 틀렸습니다. \n다시 시도해주시기 바랍니다.', content_type='text; charset=Euc-kr')