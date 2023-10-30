"""dopses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from users import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register,name='register'),
    path('', views.login,name='login'),
    path('profile/', views.profile,name='profile'),
    # path('home/', views.home,name='home'),
    path('home/', views.home,name='indexPage'),
    path('manage_proposal/', views.manage_proposal,name='manageProposalsPage'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('guidelines/', views.guidelines,name='guidelinesPage'),
    path('contact/', views.contact,name='contactPage'),
    path('changepassword/', views.change_password,name='changepasswordPage'),
    path('', include('proposal.urls')),  
    path('', include('editproposal.urls')),  
    # path('', views.login,name='login'),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
