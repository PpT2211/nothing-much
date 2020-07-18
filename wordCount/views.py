from django.http import HttpResponse
from django.shortcuts import render
import operator
from collections import OrderedDict

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['textarea']
    wordList = fulltext.split()
    wordDictionary = {}
    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
    sortedWords = sorted(wordDictionary.items(), reverse=False)
    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordList), 'sortedWords':sortedWords})
def about(request):
    return render(request, 'about.html')
