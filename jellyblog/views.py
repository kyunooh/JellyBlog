from django.http import HttpResponse

from .models import Category, Document

def index(request):
	latest_document_list = Document.objects.order_by('-document_id')[:5]
	output = ', '.join([p.document_title for p in latest_document_list])
	return HttpResponse(output)


def detail(request, document_id):
	return HttpResponse("Detail page %s." % document_id)


def category(request, category_id):
	return HttpResponse("Categoyr page %s." % category_id)

