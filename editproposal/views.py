
from django.shortcuts import render, redirect
from proposal.models import UserProposal
from .forms import ProposalForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden





def proposal_form(request, proposal_id=None):
    # Check if the user has already submitted a proposal
    if request.session.get('proposal_submitted', False):
        return HttpResponseForbidden("You cannot access the proposal form after submission.")

    if proposal_id:
        proposal = get_object_or_404(UserProposal, id=proposal_id)

        # Check if the proposal has been submitted as final
        if proposal.status == 'submitted':
            return HttpResponseForbidden("You cannot edit a submitted proposal.")

        # Ensure the proposal belongs to the current user
        if proposal.user != request.user:
            return HttpResponseForbidden("You do not have permission to edit this proposal.")

        if request.method == 'POST':
            form = ProposalForm(request.POST, instance=proposal)
            if form.is_valid():
                if form.cleaned_data['status'] == 'submitted':
                    # If user selects 'submitted,' update the status and redirect to success page
                    proposal.status = 'submitted'
                    proposal.save()
                    return redirect('submission_success')
                else:
                    # If user selects 'draft,' update the status and save as draft
                    proposal.status = 'draft'
                    proposal.save()
                return redirect('proposal_list')
            else:
                return render(request, 'proposals/proposal_form.html', {'form': form})
        else:
            form = ProposalForm(instance=proposal)
    else:
        if request.method == 'POST':
            form = ProposalForm(request.POST)
            if form.is_valid():
                proposal = form.save(commit=False)
                proposal.user = request.user
                if form.cleaned_data['status'] == 'submitted':
                    # If user selects 'submitted,' save as final submission
                    proposal.status = 'submitted'
                    proposal.save()
                    return redirect('submission_success')
                else:
                    # If user selects 'draft,' save as draft
                    proposal.status = 'draft'
                    proposal.save()
                return redirect('proposal_list')
            else:
                return render(request, 'proposals/proposal_form.html', {'form': form})
        else:
            form = ProposalForm()

    return render(request, 'proposals/proposal_form.html', {'form': form})



def proposal_list(request):
    proposals = UserProposal.objects.filter(user=request.user)
    # proposals = proposals.annotate(user_name=F('user__username'))
    return render(request, 'proposals/proposal_list.html', {'proposals': proposals})

# proposals/views.py



def submission_success(request):
    # Set a session variable to indicate that the user has successfully submitted a proposal
    request.session['proposal_submitted'] = True
    return render(request, 'proposals/submission_success.html')

