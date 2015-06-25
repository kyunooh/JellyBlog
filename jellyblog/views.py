from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Document


def sorted_category():
    return_category = list(Category.objects.all())
    childList = []
    for category in return_category:
        if (category.parent.id == 1):
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
    return redirect('/page/1')


def index_with_page(request, page):
    document_list = list(Document.objects.all())
    document_list.reverse()
    paginator = Paginator(document_list, 4)
    documents = get_documents(paginator, page)
    context = {'documents': documents, 'category_list': categoryList, 'page_range': get_page_number_range(
        paginator, documents)}
    return render(request, 'jellyblog/index.html', context)


def category_detail(request, category_id):
    return redirect("/category/" + category_id + "/page/1")


def category_with_page(request, category_id, page):
    selectedCategory = Category.objects.get(id=category_id)
    document_list = []
    if (selectedCategory.parent == categoryList[0]):
        children = Category.objects.all().filter(parent=selectedCategory.id)
        for child in children:
            document_list += Document.objects.all().filter(category_id=child.id)
    document_list += Document.objects.all().filter(category=category_id)
    document_list.sort(key=id, reverse=True)
    paginator = Paginator(document_list, 4)
    documents = get_documents(paginator, page)
    context = {'documents': documents, 'category_list': categoryList, 'category_id': category_id,
               'page_range': get_page_number_range(paginator, documents)}
    return render(request, 'jellyblog/category.html', context)


def get_documents(paginator, page):
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)
    return documents


def get_page_number_range(paginator, page):
    print(paginator.num_pages)
    if (paginator.num_pages < 11):
        return range(1, paginator.num_pages+1)
    elif (page.number - 5 > 1):
        if (page.number + 4 < paginator.num_pages):
            return range(page.number - 5, page.number + 5)
        else:
            return range(page.number - 5, paginator.num_pages + 1)
    else:
        return range(1,11)

def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    document.view_count += 1
    document.save()
    return render(request, 'jellyblog/detail.html', {'document': document, 'category_list': categoryList})
