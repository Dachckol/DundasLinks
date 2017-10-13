from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from contact.forms import ContactForm
from contact.models import ContactEntry
from django.core.mail import send_mail
from django.contrib import messages


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = ContactEntry.objects.create(name=form.cleaned_data["name"],
                                                       email=form.cleaned_data[
                "email"],
                contentType=form.cleaned_data[
                "contentType"],
                content=form.cleaned_data["content"])
            contact.save()
            send_mail("Change at Dundas Links", "There has been some sort of change in the DWD admin page. Better have a look...",
                      "site@dundaslinks.co.uk", ["dackomichal@gmail.com"], fail_silently=True)
            messages.success(request, "Your form was sent! Expect a reply within 48 hours.")

            return HttpResponseRedirect('/')
        else:
            return render_to_response("contact.html", {"form": form},
                                      context_instance=RequestContext(request))
    else:
        # user is not submitting the form, show them a registration form
        form = ContactForm()
        context = {"form": form}
        return render_to_response('contact.html', context,
                                  context_instance=RequestContext(request))