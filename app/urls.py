from django.urls import path, include
from .views import *

urlpatterns = [
    path('auditors/', auditors),
    path('login/', LoginUser.as_view()),
    path('logout/', logout_user),
    path('api/auditors/', AuditorAPI.as_view()),
    path('api/bron', BronAPI.as_view()),
    path('day/<int:year>/<int:month>/<int:day>/', bron),
    path('', bron, name='home'),
    path('', include('django.contrib.auth.urls')),

]