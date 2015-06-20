from django.shortcuts import render, get_object_or_404
from .models import Category, Document




def sorted_category():
    return_category = list(Category.objects.all())
    print(return_category)
    for category in return_category:
        print(category)
        if(category.is_child == False):
            print("in if category : " + str(category) + ", category id: "+ str(category.id))
            continue
        else:
            parent_index = return_category.index(find_parent(return_category,category))
            print(parent_index)
            return_category[parent_index].children.append(category)
            return_category.remove(category)
    print(return_category)
    return return_category

def find_parent(category_list, category):
    for child in category_list:
        if(child.id == category.parent):
            return child



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


def category(request, category_id):
    document = get_object_or_404(Category, pk=category_id)
    return render(request, 'jellyblog/category.html',{'category_list': categoryList})

def category_detail(request, category_id):
    document_list = Document.objects.all().filter(category=category_id).order_by('-id')[:5]
    return render(request, 'jellyblog/index.html',{'document_list': document_list,'category_list': categoryList })