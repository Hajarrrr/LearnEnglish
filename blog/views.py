from django.shortcuts import render
from django.views.generic import TemplateView , ListView
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.core.exceptions import PermissionDenied 

from .models import * #,Images
from . import urls


from django.http import HttpResponse
from django.utils.translation import gettext as _

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def home(request):
    template_name = 'blog/home.html'
    all_nouns=nouns.objects.all()
    return render(request,template_name,{'nouns':all_nouns})

def listNouns(request):
    all_nouns=nouns.objects.all()
    return render(request,'blog/listNouns.html',{'nouns':all_nouns})

def test(request):
    all_nouns=nouns.objects.all()
    return render(request,'blog/test.html',{'nouns':all_nouns})

#def display_nouns_images(request): 
  
#    if request.method == 'GET': 
  
        # getting all the objects of nouns including images. 
#        all_nouns=nouns.objects.all() 
#        return render((request, 'blog/listNouns.html', {'nouns_imgs' : all_nouns}))

def tests(request):
    return render(request,'blog/tests.html')

def listVerbs(request):
    all_verbs=verbs.objects.all()
    return render(request,'blog/listVerbs.html',{'verbs':all_verbs})


def testVerbs(request):
    all_nouns=nouns.objects.all()
    return render(request,'blog/testVerbs.html',{'nouns':all_nouns})

def crosswords(request):
    all_nouns=nouns.objects.all()
    all_verbs=verbs.objects.all()
    all_cross=cross.objects.all()
    return render(request,'blog/crosswords.html',{'nouns':all_nouns,'verbs':all_verbs,'cross':all_cross})

def arabic(request):
    #output = _("Welcome to my site.")
    #return HttpResponse(output)
    all_nouns=nouns.objects.all()
    all_verbs=verbs.objects.all()
    return render(request,'blog/arabic.html',{'verbs':all_verbs,'nouns':all_nouns})