from django.conf.urls import url

from .api import transform


urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^transform/', transform, name='transform'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]