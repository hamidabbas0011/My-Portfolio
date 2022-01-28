from django.contrib import admin
from django.urls import path
from apps import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
    path('<int:pro_id>/filter/', views.project, name='project'),
    path('<int:cat_id>/cat-filter/', views.categoryList, name='categories'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
