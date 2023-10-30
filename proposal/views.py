from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout,update_session_auth_hash

from .forms import UpdateUserForm,UpdateProfileForm,CoverPageForm, Abstract_DetailsForm,Scheduling_requestForm,Instrument_SetupForm,List_Of_ObjeftsForm,Observation_StrategyForm,Attechments_DetailsForm,Publication_DetailsForm,PreviewForm





def home(request):
    return render(request, 'users/home.html')

def proposal(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
           
            proposal_form = CoverPageForm(request.POST,request.FILES, instance=request.user.userproposal.first())
            
            if proposal_form.is_valid():
                
                proposal_form.save()
                print("saved")
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='abstractPage') 
            else:
                
                print('Proposal form errors:', proposal_form.errors)
        else:
            
            proposal_form = CoverPageForm(instance=request.user.userproposal.first())
    
        return render(request, 'users/proposal.html', {'proposal_form': proposal_form})
    else:
        return redirect('login') 





#--------------------------------------------------------------------------------------------------------------------#






def abstractPage(request):

    if request.method == 'POST':
        
        proposal_form = Abstract_DetailsForm(request.POST,request.FILES, instance=request.user.userproposal.first())

        if proposal_form.is_valid():
                    
            proposal_form.save()
            print('proposal is saved')
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='schedulingPage')
    else:
        
        proposal_form = Abstract_DetailsForm(instance=request.user.userproposal.first())

    return render(request, 'users/abstract.html',{'proposal_form': proposal_form})


#--------------------------------------------------------------------------------------------------------------------#





def schedulingPage(request):

    if request.method == 'POST':

        

        proposal_form = Scheduling_requestForm(request.POST,request.FILES, instance=request.user.userproposal.first())


        if proposal_form.is_valid():
            print('this is proposal is saved')

            

            proposal_form.save()
            print("hello")
            messages.success(request, 'Your profile is updated successfully')

            return redirect(to='instrumentPage')
        else:
        
            print('Proposal form errors:', proposal_form.errors)

    else:
        
        proposal_form = Scheduling_requestForm(instance=request.user.userproposal.first())

    return render(request, 'users/scheduling.html', {'proposal_form':proposal_form})


#--------------------------------------------------------------------------------------------------------------------#




def instrumentPage(request):
    if request.method == 'POST':
        
        proposal_form = Instrument_SetupForm(request.POST,request.FILES, instance=request.user.userproposal.first())
        if proposal_form.is_valid():
            
            proposal_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='objectsPage')
        else:
            print('Proposal form errors:', proposal_form.errors)    
    else:
        
        proposal_form = Instrument_SetupForm(instance=request.user.userproposal.first())

    return render(request, 'users/instrument.html', {'proposal_form': proposal_form})


#--------------------------------------------------------------------------------------------------------------------#




def objectsPage(request):
    if request.method == 'POST':
     
        proposal_form = List_Of_ObjeftsForm(request.POST,request.FILES, instance=request.user.userproposal.first())
        if proposal_form.is_valid():
            
            proposal_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='observationPage')
    else:
        
        proposal_form = List_Of_ObjeftsForm(instance=request.user.userproposal.first())

    return render(request, 'users/objects.html', {'proposal_form': proposal_form})

#--------------------------------------------------------------------------------------------------------------------#



def observationPage(request):
    if request.method == 'POST':
        
        proposal_form = Observation_StrategyForm(request.POST,request.FILES, instance=request.user.userproposal.first())

        if proposal_form.is_valid():
            
            proposal_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='attachmentsPage')
    else:
        
        proposal_form = Observation_StrategyForm(instance=request.user.userproposal.first())

    return render(request, 'users/observation.html', { 'proposal_form': proposal_form})

#--------------------------------------------------------------------------------------------------------------------#




def attachmentsPage(request):
    if request.method == 'POST':
        print('this is post method')
        
        proposal_form = Attechments_DetailsForm(request.POST,request.FILES, instance=request.user.userproposal.first())

        if proposal_form.is_valid():
            
            print("proposal is valid")
            
            proposal_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='publicationsPage')
        else:
            print('Proposal form errors:', proposal_form.errors)  
    else:
        
        proposal_form = Attechments_DetailsForm(instance=request.user.userproposal.first())

    return render(request, 'users/attachments.html', { 'proposal_form': proposal_form})



#--------------------------------------------------------------------------------------------------------------------#





def publicationsPage(request):
    if request.method == 'POST':
       
        proposal_form = Publication_DetailsForm(request.POST,request.FILES, instance=request.user.userproposal.first())

        if proposal_form.is_valid():
          
            proposal_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='previewPage')
    else:
        
        proposal_form = Publication_DetailsForm(instance=request.user.userproposal.first())
    return render(request, 'users/publications.html', { 'proposal_form': proposal_form})



#-------------------------------------------------------------------------------------------------------------------#


# def previewPage(request):
#     if request.method == 'POST':
        
#         proposal_form = PreviewForm(request.POST,request.FILES, instance=request.user.userproposal.first())

#         if proposal_form.is_valid():
        
#             proposal_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='profile')

#         else:
#             print('Proposal form errors:', proposal_form.errors)  
#     else:
       
#         proposal_form = PreviewForm(instance=request.user.userproposal.first())

#     return render(request, 'users/preview.html', { 'proposal_form': proposal_form})



# preview.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PreviewForm  # Import both form classes
from .models import UserProposal  # Import the model if it's not already imported
from django.http import HttpResponseForbidden
from .models import UserProposal

from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProposal
from datetime import datetime

def get_cycle_code():
    current_date = datetime.now()
    if current_date.month in [4, 5, 6, 7]:
        return 'C1'
    elif current_date.month in [11, 12, 1]:
        return 'C2'
    else:
        # Add more conditions for additional cycles if needed
        return 'C3'

def previewPage(request, proposal_id=None):
    # Retrieve the user's proposal if available
    proposal = None
    if proposal_id:
        proposal = get_object_or_404(UserProposal, id=proposal_id)
        if proposal.user != request.user:
            return HttpResponseForbidden("You do not have permission to edit this proposal.")

    if request.session.get('proposal_submitted', False):
        return HttpResponseForbidden("You cannot access the proposal form after submission.")

    if request.method == 'POST':
        proposal_form = PreviewForm(request.POST, request.FILES, instance=proposal)
        if proposal_form.is_valid():
            proposal = proposal_form.save(commit=False)
            
            # Set the user for the proposal
            proposal.user = request.user

            if proposal_form.cleaned_data['status'] == 'submitted':
                # If the user selects 'submitted,' update the status and cycle code
                proposal.status = 'submitted'
                proposal.cycle_code = get_cycle_code()
                proposal.save()
                return redirect('submission_success')
            else:
                # If the user selects 'draft,' update the status and save as draft
                proposal.status = 'draft'
                proposal.save()
            return redirect('proposal_list')
    else:
        # Handle GET requests and form display
        proposal_form = PreviewForm(instance=proposal)

    return render(request, 'users/preview.html', {'proposal_form': proposal_form})




# def proposal_list(request):
#     proposals = UserProposal.objects.filter(user=request.user)
#     # proposals = proposals.annotate(user_name=F('user__username'))
#     return render(request, 'proposals/proposal_list.html', {'proposals': proposals})

#     return render(request, 'users/preview.html', {'proposal_form': proposal_form})


#-----------------------------------------------------------------------------------------------------------------




def pdfPage(request):
    return render(request, 'users/pdf.html')



#<===============================================================================>



#PDF Generate view which is importing generate_pdf views form pdfgen.py 


from .pdfgen import generate_pdf
from django.http import HttpResponse
from users.models import Profile
from .models import UserProposal
def DownloadPDF(request):
    profile = Profile.objects.get(user=request.user)

    # Filter UserProposal objects related to the user
    user_proposals = UserProposal.objects.filter(user=request.user)

    if user_proposals.exists():
        # Decide which UserProposal object to use, e.g., the first one
        proposal = user_proposals.first()

        # Get the cycle code based on your business logic (e.g., using the logic you mentioned earlier)
        cycle_code = get_cycle_code()  # Replace with your cycle code retrieval logic

        pdf = generate_pdf('users/downloadPDF.html', profile, proposal, cycle_code)

        return HttpResponse(pdf, content_type='application/pdf')
    else:
        # Handle the case where no UserProposal exists for the user
        # You can return an error message or handle it according to your requirements.
        return HttpResponse("No UserProposal found for this user.")

















