from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_page(request):
    html ="""
    <h1>First Page</h1>
    """
    return HttpResponse(html)
