from django.conf.urls import url, include
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^result/', include('result.api.urls', namespace='result_api')),
]
