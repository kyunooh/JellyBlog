from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Document


def sorted_category():
    return_category = list(Category.objects.all())
    childList = []
    for category in return_category:
        print(category)
        if(category.parent.id == 1):
            print("in if: "+ category.name)
            continue
        else:
            parent_index = return_category.index(category.parent)
            return_category[parent_index].children.append(category)
            childList.append(category)

    for child in childList:
        return_category.remove(child)

    return return_category

categoryList = sorted_category()


def index(request):
    latest_document_list = Document.objects.order_by('-id')[:5]
    context = {'document_list': latest_document_list,'category_list' : categoryList }
    return render(request, 'jellyblog/index.html', context)


def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    document.view_count += 1
    document.save()
    return render(request, 'jellyblog/detail.html', {'document': document, 'category_list': categoryList})



def category_detail(request, category_id):
    selectedCategory = Category.objects.get(id=category_id)
    document_list = []
    if(selectedCategory.parent == categoryList[0]):
        children = Category.objects.all().filter(parent=selectedCategory.id)
        for child in children:
            document_list += Document.objects.all().filter(category_id=child.id).order_by('-id')[:5]
    else:
        document_list += Document.objects.all().filter(category=category_id).order_by('-id')[:5]
    return render(request, 'jellyblog/index.html',{'document_list': document_list,'category_list': categoryList })