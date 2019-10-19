
from django.conf import settings 
from django.contrib import admin
from django.urls import path, include

from .views import home



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',home, name='home') 
    #worked in conjunction with demo/views.py, which has been 
    #removed
]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
	#just a quick way to setup the single module	