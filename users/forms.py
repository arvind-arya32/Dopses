from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from .models import Profile

# from .models import Profile


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True, 
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']



class Changepassword(PasswordChangeForm):

    old_password = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    new_password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    new_password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

class UpdateUserForm(forms.ModelForm):
    password = None
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    # added
    first_name = forms.CharField(max_length=100,
                               required=True,
                               error_messages={'required':'Enter your name'},
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']




class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    #added
    TITLE = (
        (" ","Select title"),
        ("1", "Prof."),
        ("2", "Dr."),
        ("3", "Mrs."),
        ("4", "Ms."),
        ("5", "Mr.")
    )

    DESIGNATION = (
        (" ","Select designation"),
        ("1", "Faculty/Academic."),
        ("2", "Postdoc."),
        ("3", "PhD student."),
        ("4", "Graduate student."),
        
    )
    REFEREE = (
        ("","Selct"),
        ("1", "Yes."),
        ("2", "No."),
        
        
    )

    INTERESTS=(
        ("","Select"),
        ("1", "AGN & Quasars"),
        ("2", "Compact Object Binaries"),
        ("3", "Cosmology"),
        ("4", "Earth Atmosphere"),
        ("5", "Exo-solar Planets"),
        ("6", "Galaxies"),
        ("7", "Gamma Ray Bursts"),
        ("8", "Globular Cluster"),
        ("9", "High-redshift galaxies"),
        ("10", "Individual Star"),
        ("11", "Instrumentation"),
        ("12", "Intergalactic medium"),
        ("13", "Interstellar medium"),
        ("14", "Near Earth Onjects"),
        ("15", "Open Cluster"),
        ("16", "Planetary Bodies"),
        ("17", "Solar System"),
        ("18", "Strar and Planet Formation"),
        ("19", "Supernovae"),
        ("20", "Surveys"),

    )
    AFFILIATION=(
        ("","Select"),
        ("1", "test1"),
        ("2", "test2"),
        ("3", "test3"),
        ("4", "test4"),

    )



#  affiliation_name = models.CharField(User, max_length=500, default='Unknown affiliation')




    title = forms.CharField(label='Title',
                            required=True,
                            widget=forms.Select(choices=TITLE,
                            attrs={'class':'form-control'}))



    alternate_email_id = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                                'class': 'form-control'
                                                                }))


    affiliation = forms.CharField(label='Designation',
                                  required=True,
                                  widget=forms.Select(choices=AFFILIATION,
                                  attrs={'class': 'form-control'}))



    affiliation_name = forms.CharField(max_length=500,
                                      required=True,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
  



    designation = forms.CharField(label='Designation',
                                  required=True,
                                  widget=forms.Select(choices=DESIGNATION,
                                  attrs={'class': 'form-control'}))


    act_as_referee = forms.CharField(label='Act as referee ?',
                                     required=True,
                                     widget=forms.Select(choices=REFEREE,
                                     attrs={'class': 'form-control'}))


    address = forms.CharField(max_length=1000,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone_number = forms.IntegerField(
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile_number = forms.IntegerField(
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(max_length=100,
                               
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    research_interest = forms.CharField(label='Research Interest',
                                                required=True,
                                                widget=forms.Select(choices=INTERESTS,attrs={'class': 'form-control'}),
                                                )




    class Meta:
        model = User
        fields = ['avatar','title','first_name','last_name','bio','affiliation','affiliation_name','designation', 'act_as_referee','address', 'telephone_number', 'mobile_number', 'country','state','city','alternate_email_id','research_interest']
