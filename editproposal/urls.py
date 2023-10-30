# proposals/urls.py
# proposals/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('proposals/', views.proposal_list, name='proposal_list'),
    path('proposals/new/', views.proposal_form, name='new_proposal_form'),
    path('proposals/edit/<int:proposal_id>/', views.proposal_form, name='edit_proposal_form'),
    path('proposals/success/', views.submission_success, name='submission_success'),
]
