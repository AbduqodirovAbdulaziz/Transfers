from django.shortcuts import render
from .models import *
from datetime import *


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def tryouts(request):
    return render(request, 'tryouts.html')


def stats(request):
    return render(request, 'stats.html')


def clubs(request):
    return render(request, 'clubs.html')


def seasons(request):
    mavsumlar = Transfer.objects.all().values_list('mavsum', flat=True)
    context = {
        'mavsumlar': sorted(mavsumlar)
    }
    return render(request, 'transfer-archive.html', context)


# ---------------------------------------------------
def players(request):
    context = {
        "players": Player.objects.all()
    }
    return render(request, 'players.html', context)


def clubs(request):
    context = {
        "clubs": Club.objects.all()
    }
    return render(request, 'clubs.html', context)


def country_clubs(request, country_name):
    context = {
        'clubs': Club.objects.filter(davlat__nom=country_name)
    }
    return render(request, 'country-clubs.html', context)


def katta_players(request):
    hozirgi_sana = str(date.today())
    yil = int(hozirgi_sana[:4]) - 20
    yangi_sana = hozirgi_sana.replace(hozirgi_sana[:4], str(yil))
    context = {
        "players": Player.objects.filter(t_yil__gt=yangi_sana)
    }
    return render(request, 'U-20 players.html', context)


def latest_transfers(request):
    context = {
        'transfers': Transfer.objects.order_by('-id')
    }
    return render(request, 'latest-transfers.html', context)


def clubs_player(request, club_name):
    context = {
        "players": Player.objects.filter(club=Club.objects.get(nom=club_name))
    }
    return render(request, 'clubs-players.html', context)


# ------------------------
def birinchi(request):
    return render(request, '150-accurate-predictions.html', )


def accurate_predictions(request):
    context = {
        "transfers": Transfer.objects.order_by('-narx')[:150]
    }
    return render(request, 'stats/150-accurate-predictions.html', context)


def ikkinchi(request):
    return render(request, 'top-50-clubs-by-expenditure-in-2021.html')


def uchinchi(request):
    return render(request, 'top-50-clubs-by-income-in-2021.html')


def top_50_clubs(request):
    context = {
        'clubs': Club.objects.order_by('-kapital')[:50]
    }
    return render(request, 'top-50-clubs-by-income-in-2021.html', context)


def tortinchi(request):
    return render(request, 'transfer-records.html')

def transfers_record(request):
    context={
        'players': Transfer.objects.all()
    }
    return render(request, 'transfer-records.html', context)
