from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import UserProposal



class CoverPageForm(forms.ModelForm):

    CHOICES = (
        ("ARIES (33%)",       "ARIES (33%)"),
        ("Indian Time (60%)", "Indian Time (60%)"),
        ("Belgian (7%)",      "Belgian (7%)"),
    )

    TYPE_CHOICES = (
        ("","Select Proposal Type "),
        ("Long Term (New)",    "Long Term (New)"),
        ("Long Term (Ongoing)","Long Term (Ongoing)"),
        ("Short Term",         "Short Term"),
        ("Thesis Project",     "Thesis Project"),
    )

    TARGET_CHOICES = (
        ("","Select Please "),
        ("YES", "YES"),
        ("NO", "NO"),
    )
    proposal_category = forms.CharField(label='Proposal Category', widget=forms.RadioSelect(choices=CHOICES,))

    proposal_title = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    proposal_type = forms.CharField(label='Proposal Type', widget= forms.Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'}))

    target_opportunity = forms.CharField(label='Proposal Type', widget= forms.Select(choices=TARGET_CHOICES, attrs={'class': 'form-control'}))

    co_proposers = forms.CharField(max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    co_pi = forms.CharField(max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    present_ob = forms.CharField(max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))



    class Meta:
        model = UserProposal
        fields = ['proposal_category','proposal_title','proposal_type','target_opportunity','co_proposers','co_pi','present_ob']
        exclude = ['user']

                            
    
class Abstract_DetailsForm(forms.ModelForm):
   

    TARGET_CHOICES = (
        ("","Select Please "),
        ("YES", "YES"),
        ("NO", "NO"),
    )


    abstract = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    successful_proposals = forms.CharField(label='Proposal Category', widget=forms.RadioSelect(choices=TARGET_CHOICES,))


    class Meta:
        model = UserProposal
        fields = ['abstract','successful_proposals']
        exclude = ['user']






class Scheduling_requestForm(forms.ModelForm):


    SCHEDULING_REQUEST = (
        ("","Select Scheduling Request"),
        ("Bright", "Bright"),
        ("Grey", "Grey"),
        ("Dark", "Dark"),
        ("Time Critical Observation", "Time Critical Observation"),
        ("Other", "Other")
    )

    OBSERVING_TIME = (
        ("Hours", "Hours"),
        ("Nights", "Nights"),
    )

    


    scheduling_request = forms.CharField(label='Proposal Request', widget= forms.Select(choices=SCHEDULING_REQUEST, attrs={'class': 'form-control'}))

    observing_time = forms.CharField(required = False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    preferred_date = forms.DateField(required = False, widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}))

    impossible_date = forms.DateField(required = False, widget=forms.DateInput(attrs={'type':'date','class': 'form-control'}))

    justification = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))



    class Meta:
        model = UserProposal
        fields = ['scheduling_request','observing_time','preferred_date','impossible_date','justification']
        exclude = ['user']




class Instrument_SetupForm(forms.ModelForm):

    OBSERVATION_MODE = (
        ("","Select Observation Mode"),
        ("Imaging",                  "Imaging"),
        ("Spectroscopy",             "Spectroscopy"),
        ("Imaging and Spectroscopy", "Imaging and Spectroscopy"),
    )


    observation_mode = forms.CharField(label='Observation Mode', widget= forms.Select(choices=OBSERVATION_MODE, attrs={'class': 'form-control'}))
    

    class Meta:
        model = UserProposal
        fields = ['observation_mode']
        exclude = ['user']


class List_Of_ObjeftsForm(forms.ModelForm):
     
    list_of_objects = forms.CharField(required = False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = UserProposal
        fields =['list_of_objects']
        exclude = ['user']





class Observation_StrategyForm(forms.ModelForm):



    tech_justify = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    plans = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = UserProposal
        fields = ['tech_justify','plans']
        exclude = ['user']


class Attechments_DetailsForm(forms.ModelForm):     


    scientific_justify = forms.FileField(required= False,widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    technical_justify = forms.FileField(required = False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    ongoing_proposal_status = forms.FileField(required = False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    
    
    class Meta:
        model = UserProposal
        fields = ['scientific_justify','technical_justify','ongoing_proposal_status']
        exclude = ['user']


class Publication_DetailsForm(forms.ModelForm): 

    previous_obser = forms.CharField(required = False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    publication_relevant = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    publication_list =forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProposal
        fields = ['publication_relevant','publication_list','previous_obser']
        exclude = ['user']




class PreviewForm(forms.ModelForm):
    
    CHOICES = (
        ("ARIES (33%)",       "ARIES (33%)"),
        ("Indian Time (60%)", "Indian Time (60%)"),
        ("Belgian (7%)",      "Belgian (7%)"),
    )

    TYPE_CHOICES = (
        ("Long Term (New)",    "Long Term (New)"),
        ("Long Term (Ongoing)","Long Term (Ongoing)"),
        ("Short Term",         "Short Term"),
        ("Thesis Project",     "Thesis Project"),
    )

    TARGET_CHOICES = (
        ("YES", "YES"),
        ("NO", "NO"),
    )
    proposal_category = forms.CharField(label='Proposal Category', widget=forms.RadioSelect(choices=CHOICES,))

    proposal_title = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    proposal_type = forms.CharField(label='Proposal Type', widget= forms.Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'}))

    target_opportunity = forms.CharField(label='Proposal Type', widget= forms.Select(choices=TARGET_CHOICES, attrs={'class': 'form-control'}))

    co_proposers = forms.CharField(max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    co_pi = forms.CharField(max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    present_ob = forms.CharField(max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))






    TARGET_CHOICES = (
        ("YES", "YES"),
        ("NO", "NO"),
    )


    abstract = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    successful_proposals = forms.CharField(label='Proposal Category', widget=forms.RadioSelect(choices=TARGET_CHOICES,))



    SCHEDULING_REQUEST = (
        ("Bright", "Bright"),
        ("Grey", "Grey"),
        ("Dark", "Dark"),
        ("Time Critical Observation", "Time Critical Observation"),
        ("Other", "Other")
    )

    OBSERVING_TIME = (
        ("Hours", "Hours"),
        ("Nights", "Nights"),
    )

    


    scheduling_request = forms.CharField(label='Proposal Request', widget= forms.Select(choices=SCHEDULING_REQUEST, attrs={'class': 'form-control'}))

    observing_time = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    preferred_date = forms.DateField(required = False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    impossible_date = forms.DateField(required = False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    justification = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))



    OBSERVATION_MODE = (
        ("Imaging",                  "Imaging"),
        ("Spectroscopy",             "Spectroscopy"),
        ("Imaging and Spectroscopy", "Imaging and Spectroscopy"),
    )


    observation_mode = forms.CharField(label='Observation Mode', widget= forms.Select(choices=OBSERVATION_MODE, attrs={'class': 'form-control'}))


    list_of_objects = forms.CharField(required = False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))


    tech_justify = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    plans = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))




    scientific_justify = forms.FileField(required= False,widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    technical_justify = forms.FileField(required = False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    ongoing_proposal_status = forms.FileField(required = False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))


    
    previous_obser = forms.CharField(required = False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    publication_relevant = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    publication_list =forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    STATUS_CHOICES = (
        ('draft', 'Save as Draft'),
        ('submitted', 'Submit'),
    )
    status = forms.CharField(label='Status', widget=forms.RadioSelect(choices=STATUS_CHOICES,))


                                
    class Meta:
        model = UserProposal
        fields ='__all__'
        exclude = ['user']





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

    research_interest = forms.CharField(label='Research Interest',required=True,widget=forms.SelectMultiple(choices=INTERESTS,attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['avatar','title','first_name','last_name','bio','affiliation','affiliation_name','designation', 'act_as_referee','address', 'telephone_number', 'mobile_number', 'country','state','city','alternate_email_id']
    