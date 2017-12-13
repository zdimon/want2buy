"""want2buy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main.views import *
from django.contrib.auth import views as auth_views
from account.views import *
from archive.views import *
from feedback.views import *
from replenishment.views import replenishment_page
import api.urls as api_urls
from catalog.views import catalog_main, catalog_sub, catalog_sub_sub, annoncement_detail

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'), 
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'about/', about, name='about'),
    url(r'update/', update, name='update'),
    url(r'feedback/', feedback, name='feedback'),
    url(r'thanks/', postFeedback, name='postFeedback'),
    url(r'^user/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^user/profile/edit$', ProfileEditView.as_view(), name='profile_edit'),
    url(r'^user/registration/done', registration_done, name='registration_done'), 
    url(r'^user/activation/done', activation_done, name='activation_done'),
    url(r'^account/activate/(?P<activation_key>[-:\w]+)/$',MyActivationView.as_view(),name='registration_activate'),
    url(r'^replenishment/', replenishment_page, name='replenishment'),

    url(r'page/(?P<alias>[-:\w]+).html$', page, name='show_page'),

    url(r'^dashboard/', dashboard, name='dashboard'),
    url(r'^add_announce/', add_announce, name='add_announce'),

    url(r'^api/', include('api.urls')),

    url(r'^catalog/main/(?P<slug>[-:\w]+).html$',catalog_main,name='catalog_main'),
    url(r'^catalog/sub/(?P<slug>[-:\w]+).html$',catalog_sub,name='catalog_sub'),
    url(r'^catalog/sub/sub/(?P<slug>[-:\w]+).html$',catalog_sub_sub,name='catalog_sub_sub'),
    url(r'^annoncement/detail/(?P<slug>[-:\w]+).html$',annoncement_detail,name='annoncement_detail'),

    #url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}, name='logout'),
    #url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)