from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world (request):
    # 라우팅 해줘야해 (연결)
    # 메인 앱에서 먼저 받고 여기로 보냄

    if request.method == 'POST': # 기본적으로 겟 방식으로 작동함
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!'})
