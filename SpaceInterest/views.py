

from django.views.generic import TemplateView

class HomePage(TemplateView):
    """ Home Page """
    template_name = "index.html"

class LoggedInPage(TemplateView):
    template_name = "success.html"

class LogOutView(TemplateView):
    """ Redirects to this page after logging out """
    template_name = "logout.html"
