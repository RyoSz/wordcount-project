from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, "home.html")

def eggs(request):
    return HttpResponse('EGGS')

def about(request):
    return render(request, "about.html")

def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    
    wordlist = fulltext.split()
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            # add to the dictionary
            worddictionary[word] = 1
    
    soterdWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedWords':soterdWords})

