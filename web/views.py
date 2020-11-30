from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from itreactor.settings import TEMPLATE_HOMEPAGE, TEMPLATE_ABOUT, TEMPLATE_SERVICE, \
    TEMPLATE_BLOG,TEMPLATE_CONTACT, TEMPLATE_ELEMENTS


# Create your views here.
@csrf_protect
def home(request):
    context = {}
    context.update(csrf(request))
    return render(request, TEMPLATE_HOMEPAGE, context)


@csrf_protect
def about(request):
    context = {}
    context.update(csrf(request))
    return render(request, TEMPLATE_ABOUT, context)


@csrf_protect
def service(request):
    context = {}
    context.update(csrf(request))
    return render(request, TEMPLATE_SERVICE, context)


@csrf_protect
def blog(request):
    context = {}
    context.update(csrf(request))
    return render(request, TEMPLATE_BLOG, context)


@csrf_protect
def contact(request):
    context = {}
    context.update(csrf(request))
    return render(request, TEMPLATE_CONTACT, context)

