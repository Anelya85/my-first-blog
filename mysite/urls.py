from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'', include('blog.urls')),
	url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
]

if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns() + static(
		settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
