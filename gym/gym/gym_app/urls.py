from django.urls import path

from gym.gym_app.views import HomeView, AboutView, FeaturesView, ClassesView, ContactView, BlogView, SingleView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('features/', FeaturesView.as_view(), name='features'),
    path('classes/', ClassesView.as_view(), name='classes'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('single/', SingleView.as_view(), name='single'),

]
