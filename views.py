from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .models import Knihovna
from .serializers import KnihovnaSerializer


def knihovna_tabulka(request):
    knihovna_list = Knihovna.objects.all()
    Knihovna.auto_doplneni()
    return render(request, 'knihovna_tabulka.html', {'knihovna_list': knihovna_list})


def prodlouzit_vypujcku(request, knihovna_id):
    kniha = Knihovna.objects.get(pk=knihovna_id)
    kniha.prodlouzit_vypujcku()
    return HttpResponseRedirect(reverse('tabulka'))


class KnihovnaViewSet(viewsets.ModelViewSet):
    queryset = Knihovna.objects.all()
    serializer_class = KnihovnaSerializer
