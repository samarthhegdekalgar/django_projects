from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header = 'Tarzan Skills'
admin.site.index_title = 'Library Administrator'
admin.site.site_title = 'TarzanSkills Reference Center'

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('', include('LibraryManagement.urls')),
]

urlpatterns += staticfiles_urlpatterns()
