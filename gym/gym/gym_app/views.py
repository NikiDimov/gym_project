from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class FeaturesView(TemplateView):
    template_name = 'feature.html'


class ClassesView(TemplateView):
    template_name = 'class.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class SingleView(TemplateView):
    template_name = 'single.html'
