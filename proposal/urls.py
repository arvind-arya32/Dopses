from django.urls import path
from proposal import views
from django.urls import path
from . import views





urlpatterns = [
    path('', views.home, name='users-home'),
    # path('register/',views.Register(), name='users-register'),
    path('proposal/', views.proposal, name='users-proposal'),
    path('abstract/', views.abstractPage, name='abstractPage'),
    path('attachments/', views.attachmentsPage, name='attachmentsPage'),
    path('objects/', views.objectsPage, name='objectsPage'),
    path('instrument/', views.instrumentPage, name='instrumentPage'),
    path('observation/', views.observationPage, name='observationPage'),
    path('preview/', views.previewPage, name='previewPage'),
    path('publications/', views.publicationsPage, name='publicationsPage'),
    path('scheduling/', views.schedulingPage, name='schedulingPage'),
    path('pdf/',  views.pdfPage,name='pdfPage'),
    # Inside your Django project's urls.py



    # Your other URL patterns
    path('preview/<int:proposal_id>/', views.previewPage, name='previewPage'),
    # Your other URL patterns



    path('downloadPDF/', views.DownloadPDF, name='downloadPDF'),



    # path('testprofile/', views.testprofile, name='testprofile'),
]
