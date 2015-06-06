from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Category, Document

def index(request):
	latest_document_list = Document.objects.order_by('-document_id')[:5]
	template = loader.get_template('jellyblog/index.html')
	context = RequestContext(request, {
		'latest_document_list' : latest_document_list,
	})
	return HttpResponse(template.render(context))


def detail(request, document_id):
	return HttpResponse("Detail page %s." % document_id)


def category(request, category_id):
	return HttpResponse("Categoyr page %s." % category_id)

