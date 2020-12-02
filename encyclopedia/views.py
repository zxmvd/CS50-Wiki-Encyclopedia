import random
from django.forms import Textarea
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
from markdown2 import Markdown

markdowner = Markdown()

class KeyWordForm(forms.Form):
    keyword = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='')

class NewEntryForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control w-75'}),label="Title:")
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control w-75'}), label="Content")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form" : KeyWordForm()
    })

# render a page that displays the contents of that entry.
def entry(request, title):
    content = util.get_entry(title)
    if content != None:
        entry = markdowner.convert(content)
    else:
        entry = None
    return render(request, "encyclopedia/title.html", {
        "entry": entry,
        "title": title,
        "form": KeyWordForm()
        })

def search(request):
    list = util.list_entries()
    matches = []
    if request.method == "POST":
        form = KeyWordForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data["keyword"]
            for item in list:
                # If the query matches the name of an entry, redirect to entry page :
                if keyword.lower() == item.lower():
                    return HttpResponseRedirect(reverse('entry', kwargs={'title': item}))
                # If the query matches the title partially,
                # list the titles have the query as a substring. 
                else:
                    if keyword.lower() in item.lower():
                        matches.append(item)
            return render(request, "encyclopedia/search.html", {
            "match": matches,
            "form" : KeyWordForm()
            })
       
                
def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html", {
        "form" : KeyWordForm(),
        "form2" : NewEntryForm()
        })
    else:
        # save new entry if it doesn't exist
        list = util.list_entries()
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            for s in list:
                # if entry already exist
                if title.lower() == s.lower():
                    return render(request, "encyclopedia/erro.html", {
                        "form" : KeyWordForm(),
                        "title" : s,
                    })
            util.save_entry(title, content)

        return render(request, "encyclopedia/title.html", {
        "entry": util.get_entry(title),
        "title": title,
        "form" : KeyWordForm()
        })

def edit(request, title):
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html", {
        "content": util.get_entry(title),
        "title": title,
        "form" : KeyWordForm()
        })
    else:
        newContent = request.POST["newContent"]
        util.save_entry(title, newContent)
        return HttpResponseRedirect(reverse('entry', kwargs={'title': title}))


def randomPage(request):
    list = util.list_entries()
    title = random.choice(list)
    return HttpResponseRedirect(reverse('entry', kwargs={'title': title}))

