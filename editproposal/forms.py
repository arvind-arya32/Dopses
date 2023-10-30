# proposals/forms.py
from django import forms
from proposal.models import UserProposal

class ProposalForm(forms.ModelForm):
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
        fields = '__all__'
        exclude = ['user'] 

