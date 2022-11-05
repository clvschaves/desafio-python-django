from .forms import ShirinkForm
from .models import Web_URL
from .util import to_base_62, to_base_10
import random, string

from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


def shrink_url(request):
    context = {}
    if request.method == 'POST':
        form = ShirinkForm(request.POST)
        if form.is_valid():
            short = '' .join (random.choice(string.ascii_letters) for x in range(10))
            url = form.cleaned_data['url']
            web_url = Web_URL(url=url, short = short)
            web_url.save()
            context['short_url']= 'Rob.to/' + short
    else:
        form = ShirinkForm()
    context['form'] = form
    return render(request, 'encurtador/index.html', context)


def redirect(request, short):
    if request.method == 'GET':
        decoded_string = short
        web_url = get_object_or_404(Web_URL,short=decoded_string)
        web_url.count += 1 # Counts usages
        web_url.save()

        return HttpResponseRedirect(web_url.url)