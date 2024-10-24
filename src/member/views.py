from datetime import datetime
from django.shortcuts import render



def maliste(request):
    context = {"books": ["book1", "book2"],
               "numberMedia": 2,
    }

    return render (request, "member/list-media.html", context)