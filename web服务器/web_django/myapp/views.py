from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    file_list = []
    f = open("E:/python/code/qiubai.txt")
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


