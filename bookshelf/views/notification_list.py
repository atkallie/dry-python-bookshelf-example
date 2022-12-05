from dependencies import Package

from django.views.generic import TemplateView


repositories = Package("bookshelf.repositories")


class NotificationListView(TemplateView):
    template_name = "notification_list.html"

    @property
    def extra_context(self):
        return {"notifications": repositories.load_notifications(self.request.profile_id)}
