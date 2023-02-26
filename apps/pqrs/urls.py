from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    path('tipospqs/', views.tipospqs, name='tipospqs'),
    path('detalleTipospq/<id>', views.detalleTipospq, name='detalleTipospqn'),

    path('categoria2/', views.categoria2, name='categoria2'),
    path('registroCategoria/', views.registroCategoria, name='registroCategoria'), 
    path('edicionCategorias/', views.edicionCategorias, name='edicionCategorias'),
    path('editaCategoria/<id>', views.editaCategoria, name='editaCategoria'),
    path('eliminacionCategoria/<id>', views.eliminacionCategoria, name='eliminacionCategoria'),
     

    path('categoria1/', views.categoria1, name='categoria1'),
    path('registroTipospq/', views.registroTipospq, name='registroTipospq'), 
    
    path('verTipospq/<id>', views.verTipospq, name='verTipospq'),
    path('editaTipospq/<id>', views.editaTipospq, name='editaTipospq'),
    path('eliminacionTipospq/<id>', views.eliminacionTipospq, name='eliminacionTipospq'),
   
    path('about/', views.about, name='about'),
    path('registroListas/<id>', views.registroListas, name='registroListas'), 
    #Validaciones 
    re_path(r'^validarFecha/$', views.validarFecha, name='validarFecha'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
