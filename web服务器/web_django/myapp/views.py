from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    file_list = []
<<<<<<< HEAD
    f = open("E:/python/code/qiubai.txt")
=======
    f = open("E:/python/code/爬虫/qiubai.txt")
>>>>>>> wen服务器
    while True:
        lines = f.readlines(100)
        if not lines:
            break
        for line in lines:
            file_list.append(line.strip("'\n'").strip('\''))
            # file_list.append(line)

    f.close()
    # print(file_list)
    file_dic = {"file": str(file_list)}
    print(file_dic)
    return render(request, './myapp/index.html', file_dic)

<<<<<<< HEAD

=======
def set_cookie(request):
    '''设置cookie'''
    res = HttpResponse("设置cookie")
    res.set_cookie('hello', 'cookie', expires=60 * 60 * 24 * 7)
    return res
    
def get_cookie(request):
    '''获取cookie'''
    get = request.COOKIES.get('hello')
    if get:
        return HttpResponse('hello: ' + get)
    else:
        return HttpResponse('cookie不存在')

def set_session(request):
    '''设置session'''
    request.session['hi'] = 'session'
    return HttpResponse('设置session')
    
def get_session(request):
    get = request.session['hi']
    if get:
        return HttpResponse('hi: ' + get)
    else:
        return HttpResponse('session不存在')
>>>>>>> wen服务器
