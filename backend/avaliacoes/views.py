from django.shortcuts import render

from .models import Avaliacoes

def listar_avaliacoes(request):
    avaliacoes = Avaliacoes.objects.all().values("nome", 'nota')
    return JsonResponse(list(avaliacoes), safe=False)