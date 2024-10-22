from django.shortcuts import render


def maliste(request):
    return render(request, "list-media.html")