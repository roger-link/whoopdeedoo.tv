from django.contrib import admin

from django.conf.urls.defaults import patterns
from django.views.generic import TemplateView

admin.autodiscover()
 
urlpatterns = patterns('',
    (r'^test_static/', TemplateView.as_view(template_name="test_static.html")),
    (r'^admin/', include(admin.site.urls)),

)


















