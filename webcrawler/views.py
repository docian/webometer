from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup as BS
import requests
from langdetect import detect


# Create your views here.
from requests.exceptions import InvalidSchema


def home(request):
    print('reached home')
    return HttpResponse("<b>welcome home</b>")

def webcrawler(request, url_path):
    print('reached webcrawler')
    doc = requests.get(url_path)
    try:
        beauty = BS(doc.text, "html.parser")
    except InvalidSchema:
        return HttpResponse(f'<p><b>url not found {url_path}</b></p>')
    l_a = beauty.find_all('a')
    answ = ''
    lang = 'not detected'
    for i in l_a:
        if len(i.text) > 40:
            answ += f'<p>{i.text}</p>'
            if lang == 'not detected':
                lang = detect(i.text)
    return HttpResponse(f'<h2><b>Language:{lang}</b></h2><p>Titles:\n {answ}</p>')
