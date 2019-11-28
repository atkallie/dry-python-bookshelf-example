from dependencies import Injector
from dependencies import operation
from dependencies import Package
from dependencies import this
from dependencies.contrib.django import view
from django.utils.translation import gettext as _


implemented = Package("bookshelf.implemented")
functions = Package("bookshelf.functions")


@view
class CategoryDetailView(Injector):

    template_name = "category_detail.html"

    show_category = implemented.ShowCategory.show

    category_id = this.kwargs["id"]

    render = functions.Render.do

    @operation
    def get(show_category, category_id, user, render):

        result = show_category.run(category_id=category_id, user=user)
        if result.is_success:
            return render(result.value)
        elif result.failed_on("find_subscription"):
            return render(
                {
                    "category": result.ctx.category,
                    "error": _("You should subscribe to this category."),
                }
            )
        elif result.failed_on("check_expiration"):
            return render(
                {
                    "category": result.ctx.category,
                    "error": _("Your subscription expires."),
                }
            )