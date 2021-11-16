from django.shortcuts import HttpResponse
from .translate import translate

# Create your views here.


def get_only_text(request, inp, out):

    if request.method == "GET":
        text = request.GET.get('text')

        result = translate(text, inp, out)
        return HttpResponse(result)
