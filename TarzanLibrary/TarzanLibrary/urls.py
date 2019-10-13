from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Tarzan Skills'
admin.site.index_title = 'Library Administrator'
admin.site.site_title = 'TarzanSkills Reference Center'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LibraryManagement.urls'))
]
