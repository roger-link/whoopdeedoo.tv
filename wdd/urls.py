
from django.conf.urls.defaults import patterns
from django.views.generic import TemplateView
 
urlpatterns = patterns('',
    (r'^test_static/', TemplateView.as_view(template_name="test_static.html")),
)


















