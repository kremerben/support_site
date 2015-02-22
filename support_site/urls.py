from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from support_main.v1.api import views


admin.autodiscover()


urlpatterns = [
    url(r'^api/v1/', include('support_main.v1.urls', namespace='v1')),
    # Login and logout views for the browsable API
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

    # url(r'^$', 'support_user.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('support_user.urls')),
    # url(r'^ticket/', include('support_ticket.urls')),


    url(r'^$', 'support_main.views.home', name='home'),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
