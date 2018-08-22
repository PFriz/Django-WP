from django.shortcuts import render, HttpResponse

# Create your views here.

html_nav="""
<ul>
    <li><a href="/">home</a></li>
    <li><a href="/contacto/">contacto</a></li>
    <li><a href="/portafolio/">portafolio</a></li>
</ul>

"""

html_header="""
<h1>Mi web personal</h1>
"""

html_base= html_header + html_nav

def home(request):
    return render(request, "core/home.html")

def contacto(request):
    return render(request, "core/contacto.html")


def portafolio(request):
    return render(request, "core/portafolio.html")

