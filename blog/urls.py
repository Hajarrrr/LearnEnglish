from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('index/', views.index, name='index'),

    path('listNouns/', views.listNouns, name='blog-listNouns'),
    path('test/', views.test, name='blog-test'),
    path('listNouns/test/', views.test, name='blog-test'),
    path('listNouns/', views.test, name='blog-test'),

    path('listNouns/test/listVerbs/', views.listVerbs),
    path('listNouns/test/listVerbs/testVerbs/', views.testVerbs, name='blog-testVerbs'),
    path('listNouns/test/listVerbs/testVerbs/crosswords/', views.crosswords, name='blog-crosswords'),

    
    path('testVerbs/', views.testVerbs, name='blog-testVerbs'),
    path('listVerbs/testVerbs/', views.testVerbs, name='blog-testVerbs'),


    path('listNouns/listVerbs/', views.listVerbs, name='blog-listVerbs'),
    path('listNouns/listVerbs/tests/', views.tests, name='blog-tests'),
    path('listNouns/listVerbs/tests/test/', views.test, name='blog-test'),
    path('listNouns/listVerbs/tests/testVerbs/', views.testVerbs, name='blog-testVerbs'),
    path('listNouns/listVerbs/tests/crosswords/', views.crosswords, name='blog-crosswords'),


    path('listVerbs/', views.listVerbs, name='blog-listVerbs'),
    
    path('crosswords/', views.crosswords, name='blog-crosswords'),
    
    
    path('arabic/', views.arabic, name='blog-arabic'),

]

#path('nouns_imgs', views.display_nouns_images, name = 'nouns_imgs'),

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)