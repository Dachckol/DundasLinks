from django.shortcuts import render_to_response
from django.template import RequestContext
from news.models import Entry


def home(request):
    entries = Entry.objects.all().order_by("-pub_date")[:5]
    context = {"entries":entries}
    template = "index.html"
    return render_to_response(template,
                              context,
                              context_instance=RequestContext(request))

def about(request):
    context = {}
    template = "about.html"
    return render_to_response(template, context)


def products(request):
    context = {}
    template = "products.html"
    return render_to_response(template,
                              context,
                              context_instance=RequestContext(request))


def order(request):
    context = {}
    template = "pricing.html"
    return render_to_response(template,
                              context,
                              context_instance=RequestContext(request))
