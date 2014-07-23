#coding:utf-8

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from polls.models import Poll

#各ビューは次の2つのいずれかを実行する
#1. HttpResponseオブジェクトを返す　
#2. Http404のような例外を送出する
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', 
            {'latest_poll_list':latest_poll_list})
    #以下と同義
    #t = loader.get_template('polls/index.html')
    #c = Context({
    #    'latest_poll_list':latest_poll_list,
    #    })
    #return HttpResponse(t.render(c))

def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p})
