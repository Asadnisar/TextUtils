from django.http import HttpResponse
from django.shortcuts import render

def index2(request):
    return render(request,'ab.html')

def analyze2(request):
    #get text
    djtxt = request.POST.get('text', 'default')
    #check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fulcap = request.POST.get('fulcap','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # chcount = request.GET.get('chcount', 'off')
   #chech which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtxt:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtxt = analyzed
        # return render(request, 'analyze.html', params)
    if fulcap == "on":
        analyzed = ""
        for char in djtxt:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtxt = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtxt:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtxt):
            if not (djtxt[index] == "" and djtxt[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtxt = analyzed
        # return render(request, 'analyze.html', params)

    if removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fulcap != "on":
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyzer2.html', params)


