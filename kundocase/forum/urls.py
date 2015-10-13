from django.conf.urls import url
from kundocase.forum.views import startpage, question

urlpatterns = [
    url(r"^$", startpage, name="startpage"),
    url(r"^(?P<id>\d+)$", question, name="question")
]
