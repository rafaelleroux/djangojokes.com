from django.urls import path

from .views import HomePageView, AboutUsPageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsPageView.as_view(), name='about-us')
]