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
from archive.views import *
from feedback.views import *
from replenishment.views import PayView, PayCallbackView, replenishment_page
import api.urls as api_urls
import account.urls as accounts_urls
from catalog.views import catalog_main, catalog_sub, catalog_sub_sub, annoncement_detail

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'), 
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^about/', about, name='about'),
    url(r'^update/', update, name='update'),
    url(r'^feedback/', feedback, name='feedback'),
    url(r'^thanks/', postFeedback, name='postFeedback'),
     url(r'^rlogin/(?P<id>[0-9]+)', rlogin),

    
    
    
    
    url(r'page/(?P<alias>[-:\w]+).html$', page, name='show_page'),

    url(r'^add_announce/', add_announce, name='add_announce'),

    url(r'^api/', include('api.urls')),

    url(r'^catalog/main/(?P<slug>[-:\w]+).html$',catalog_main,name='catalog_main'),
    url(r'^catalog/sub/(?P<slug>[-:\w]+).html$',catalog_sub,name='catalog_sub'),
    url(r'^catalog/sub/sub/(?P<slug>[-:\w]+).html$',catalog_sub_sub,name='catalog_sub_sub'),
    url(r'^annoncement/detail/(?P<slug>[-:\w]+).html$',annoncement_detail,name='annoncement_detail'),

    url(r'^pay/(?P<payment_id>)$', PayView.as_view(), name='pay_view'),
    url(r'^pay-callback/$', PayCallbackView.as_view(), name='pay_callback'),
    url(r'^replenishment/', replenishment_page, name='replenishment'),

    #url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}, name='logout'),
    #url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^user/', include('account.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^dashboard/', include('account.urls')),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)