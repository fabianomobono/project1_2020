from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
import markdown2
from markdown2 import Markdown
from . import util
from .models import NewEntryForm
from random import randrange

# this is the index function
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# this renderes when somebody clicks on a link or types in a URL
def page(request, query):
    markdowner = Markdown()
    page = util.get_entry(query)
    if page == None:
        return render(request, "encyclopedia/404.html")

    page = markdowner.convert(str(page))
    print(page)
    query = str(query)
    print(query)
    return render(request, "encyclopedia/page.html", {"page": page, "title": query })


# search function
def search(request):
    if request.method == "POST":
        # get the search term
        term = str(request.POST['q'])
        # query all the pages...this seems not efficient
        results = util.list_entries()

        # if the search matches a page call the function to render that page
        if term in results:
            return page(request, term)

        # using string comprehension
        res = [i for i in results if term in i]
        context = {
            "results": res
        }
        return render(request, "encyclopedia/results.html", context)

    else:
        return HttpResponse("Method not allowed(GETTTTTT)")


# create new page
def create(request):
    if request.method == "POST":
        title = request.POST['newpagetitle']
        text = request.POST['entry']
        current_files = util.list_entries()
        if title in current_files:
            return render(request, "encyclopedia/create_page.html", {"message": "Page already exists"})

        else:
            util.save_entry(title, text)
            return render(request, "encyclopedia/create_page.html", {"message": "Entry saved"})
    return render(request, "encyclopedia/create_page.html")


# edit page
def edit(request):
    if request.method =="POST":
        title = request.POST['title']
        edit = request.POST['edit']
        util.save_entry(title, edit)
        return page(request, title)
    else:
        x = request.GET['x']
        original_text = util.get_entry(x)
        print(x)
        return render(request, "encyclopedia/edit.html", {"title": x, 'text': original_text})



def random(request):
    pages = util.list_entries()
    number = randrange(0, len(pages))
    print(number)

    result = pages[number]

    return page(request, result)
