from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.conf import settings
from .models import Document


class DocumentList(ListView):
    model = Document
    template_name = 'lifeblog/index.html'

    def get_context_data(self, **kwargs):
        context = super(DocumentList, self).get_context_data(**kwargs)
        context['test'] = settings.TEST
        return context

    
class DocumentDetail(DetailView):
    queryset = Document.objects.all()

    def get_object(self, **kwargs):
        object = super(DocumentDetail, self).get_object(**kwargs)
        return object

    def get_context_data(self, **kwargs):
        context = super(DocumentDetail, self).get_context_data(**kwargs)
        context['test'] = settings.TEST
        return context
        
