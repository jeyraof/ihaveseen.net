from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

import ihaveseen.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', ihaveseen.views.MainView.as_view(), name='main'),
]
