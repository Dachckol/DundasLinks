from django.shortcuts import render_to_response
from news.models import Entry
from django.template import RequestContext


def home(request):
    template = "news.html"
    entries = Entry.objects.all().order_by("-pub_date")
    context = {"entries": entries}
    return render_to_response(template,
                              context,
                              context_instance=RequestContext(request))
