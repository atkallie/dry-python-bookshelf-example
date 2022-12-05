from dependencies import Package

from django.views.generic import TemplateView


repositories = Package("bookshelf.repositories")


class CategoryListView(TemplateView):
    template_name = "category_list.html"

    @property
    def extra_context(self):
        return {"categories": repositories.load_subscribed_categories(self.request.profile_id)}
