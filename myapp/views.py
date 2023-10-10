from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect
from django.http import HttpRequest
from typing import Union, Sequence, Optional, Mapping, Any

def home(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="base.html")
