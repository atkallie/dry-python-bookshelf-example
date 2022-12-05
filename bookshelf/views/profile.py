from dependencies import Package

from django.views.generic import TemplateView


repositories = Package("bookshelf.repositories")


class ProfileView(TemplateView):
    template_name = "profile.html"

    @property
    def extra_context(self):
        return {"profile": repositories.load_profile(self.request.profile_id)}
