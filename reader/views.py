from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import requests
import configparser
from dateutil import parser

temp_img = "https://images.pexels.com/photos/3225524/pexels-photo-3225524.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500"
#  https://www.w3schools.com/code/tryit.asp?filename=GJ8R42LMFRLP
CONFIG = configparser.ConfigParser()
def home(request):
    page = request.GET.get('page', 1)
    search = request.GET.get('search', None)

    if search is None or search=="top":
        # get the top news
        url = "https://newsapi.org/v2/top-headlines?country={}&page={}&apiKey={}&language=en".format(
            "in",1,settings.APIKEY
        )
    else:
        # get the search query request
        url = "https://newsapi.org/v2/everything?qInTitle={}&sortBy=publishedAt&page={}&apiKey={}&country{}&language=en".format(
            search, page, settings.APIKEY, "in"
        )
    r = requests.get(url=url)
    
    data = r.json()
    if data["status"] != "ok":
        return HttpResponse("<h1>Request Failed</h1>")
    data = data["articles"]
    context = {
        "success": True,
        "data": [],
        "search": search
    }
    # seprating the necessary data
    for i in data:
        context["data"].append({
            "title": i["title"],
            "description": "" if i["description"] is None else i["description"],
            "url": i["url"],
            "image": temp_img if i["urlToImage"] is None else i["urlToImage"],
            "publishedAt": parser.isoparse(i['publishedAt']).strftime('%Y-%m-%d %H:%M'),
            #"publishedAt": i["publishedAt"],
            "source": i["source"]
        })
    # send the news feed to template in context
    return render(request, 'index.html', context=context)


def loadcontent(request):
    try:
        page = request.GET.get('page', 1)
        search = request.GET.get('search', None)
        # url = "https://newsapi.org/v2/everything?q={}&sortBy={}&page={}&apiKey={}".format(
        #     "Technology","popularity",page,settings.APIKEY
        # )
        if search is None or search=="top":
            url = "https://newsapi.org/v2/top-headlines?country={}&page={}&apiKey={}&language={}".format(
                "in",page,settings.APIKEY,"en"
            )
        else:
            url = "https://newsapi.org/v2/everything?q={}&sortBy=publishedAt&page={}&apiKey={}".format(
                search,page,settings.APIKEY
            )
        print("url:",url)
        r = requests.get(url=url)
        
        data = r.json()
        if data["status"] != "ok":
            return JsonResponse({"success":False})
        data = data["articles"]
        context = {
            "success": True,
            "data": [],
            "search": search
        }
        for i in data:
            context["data"].append({
                "title": i["title"],
                "description": "" if i["description"] is None else i["description"],
                "url": i["url"],
                "image": temp_img if i["urlToImage"] is None else i["urlToImage"],
                "publishedAt": parser.isoparse(i['publishedAt']).strftime('%Y-%m-%d %H:%M'),
                #"publishedAt": i["publishedAt"],
                "source": i["source"]
            })

        return JsonResponse(context)
    except Exception as e:
        return JsonResponse({"success":False})


def cat(request):
    page = request.GET.get('page', 1)
    category = request.GET.get('category', None)

    if category is None or category == "top":
        # get the top news
        url = "https://newsapi.org/v2/top-headlines?country={}&page={}&apiKey={}".format(
            "in", 1, settings.APIKEY
        )
    else:
        # get the search query request
        url = "https://newsapi.org/v2/top-headlines?category={}&apiKey={}&country={}&language={}".format(
            category, settings.APIKEY,"in","en"

        )
    r = requests.get(url=url)

    data = r.json()
    if data["status"] != "ok":
        return HttpResponse("<h1>Request Failed type Something in the Searchbar</h1>")
    data = data["articles"]
    context = {
        "success": True,
        "data": [],
        "category": category
    }
    # seprating the necessary data
    for i in data:
        context["data"].append({
            "title": i["title"],
            "description": "" if i["description"] is None else i["description"],
            "url": i["url"],
            "image": temp_img if i["urlToImage"] is None else i["urlToImage"],
            "publishedAt": parser.isoparse(i['publishedAt']).strftime('%Y-%m-%d %H:%M'),
            #"publishedAt": i["publishedAt"],
            "source": i["source"]
        })
    # send the news feed to template in context
    return render(request, 'index.html', context=context)



def con(request):
    page = request.GET.get('page', 1)
    country = request.GET.get('country', None)

    if country is None or country == "in":
        # get the top news
        url = "https://newsapi.org/v2/top-headlines?country={}&page={}&apiKey={}".format(
            "in", 1, settings.APIKEY
        )
    else:
        # get the search query request
        url = "https://newsapi.org/v2/top-headlines?country={}&apiKey={}".format(
            country, settings.APIKEY

        )
    r = requests.get(url=url)

    data = r.json()
    if data["status"] != "ok":
        return HttpResponse("<h1>Request Failed</h1>")
    data = data["articles"]
    context = {
        "success": True,
        "data": [],
        "country": country,
    }
    # seprating the necessary data
    for i in data:
        context["data"].append({
            "title": i["title"],
            "description": "" if i["description"] is None else i["description"],
            "url": i["url"],
            "image": temp_img if i["urlToImage"] is None else i["urlToImage"],
            "publishedAt": parser.isoparse(i['publishedAt']).strftime('%Y-%m-%d %H:%M'),
            #"publishedAt": i["publishedAt"],
            "source": i["source"]
        })
    # send the news feed to template in context
    return render(request, 'index.html', context=context)


def so(request):
    page = request.GET.get('page', 1)
    sources = request.GET.get('sources', None)

    if sources is None:
        # get the top news
        url = "https://newsapi.org/v2/top-headlines?country={}&page={}&apiKey={}".format(
            "in", 1, settings.APIKEY
        )
    else:
        # get the search query request
        url = "https://newsapi.org/v2/everything?sources={}&apiKey={}&language=en".format(
            sources, settings.APIKEY

        )
    r = requests.get(url=url)

    data = r.json()
    if data["status"] != "ok":
        return HttpResponse("<h1>Request Failed type Something in the Searchbar</h1>")
    data = data["articles"]
    context = {
        "success": True,
        "data": [],
        "sources": sources,
    }
    # seprating the necessary data
    for i in data:
        context["data"].append({
            "title": i["title"],
            "description": "" if i["description"] is None else i["description"],
            "url": i["url"],
            "image": temp_img if i["urlToImage"] is None else i["urlToImage"],
            "publishedAt": parser.isoparse(i['publishedAt']).strftime('%Y-%m-%d %H:%M'),
            #"publishedAt": i["publishedAt"],
            "source": i["source"]
        })
    # send the news feed to template in context
    return render(request, 'index.html', context=context)


def sub(request):
    return render(request,"contact.html")
