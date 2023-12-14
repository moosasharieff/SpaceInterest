
from django.views.generic import TemplateView

class HomePage(TemplateView):
    """ Home Page """
    template_name = "index.html"

class LoggedInPage(TemplateView):
    template_name = "success.html"