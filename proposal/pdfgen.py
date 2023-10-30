from io import BytesIO
from unittest import result
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from users.models import Profile
from .models import UserProposal


def generate_pdf(template_source, profile, proposal,cycle_code):
    template = get_template(template_source)
    context_dict = {
        'profile': profile,
        'proposal': proposal,
        'cycle_code': cycle_code,
    }
    html = template.render(context_dict)

    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")

    return None