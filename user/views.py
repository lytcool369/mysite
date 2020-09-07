from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import user.models as userModels


def joinform(request):
    return render(request, 'user/joinform.html')


def join(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']

    userModels.insert(name, email, password, gender)

    return render(request, 'user/joinsuccess.html')


def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')


def loginform(request):
    return render(request, 'user/loginform.html')


def login(request):
    email = request.POST['email']
    password = request.POST['password']

    result = userModels.fetchone(email, password)

    if result is None:
        data = {'result': 'fail'}
        return render(request, 'user/loginform.html', data)

    # 로그인 처리
    request.session['authuser'] = result

    return HttpResponseRedirect('/main')


def logout(request):
    del request.session['authuser']

    return HttpResponseRedirect('/main')


def updateform(request):
    no = request.session['authuser']['no']

    result = userModels.fetchone_no(str(no))
    data = {'user': result}

    return render(request, 'user/updateform.html', data)


def update(request):
    name = request.POST['name']
    password = request.POST['password']
    gender = request.POST['gender']
    no = request.session['authuser']['no']

    userModels.update(name, password, gender, no)
    request.session['authuser'] = {'no': no, 'name': name}

    return HttpResponseRedirect('/main')