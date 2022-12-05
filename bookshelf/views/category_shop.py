from dependencies import Package

from django.views.generic import TemplateView


repositories = Package("bookshelf.repositories")


class CategoryShopView(TemplateView):
    template_name = "category_shop.html"

    @property
    def extra_context(self):
        categories = repositories.load_categories_for_purchase(self.request.profile_id)
        prices = repositories.load_cheapest_prices_for_categories(categories)
        return {"categories": categories, "prices": prices}
