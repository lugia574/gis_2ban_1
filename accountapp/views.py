from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world (request):
    # 라우팅 해줘야해 (연결)
    # 메인 앱에서 먼저 받고 여기로 보냄

#base.html 로 보내줘
    return render(request, 'base.html')

