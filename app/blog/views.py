from django.http import HttpResponse

from django.shortcuts import render
from django.utils import timezone


def post_list(request):
    current_time = timezone.now()
    return HttpResponse(
        '<html>'
        '<body>'
        '<h1>Post List</h1>'
        '<p>{}</p>'
        '</body>'
        '</html>'.format(
            current_time.strftime('%Y. %m. %d<br>%H:%M:%S')
        )
    )