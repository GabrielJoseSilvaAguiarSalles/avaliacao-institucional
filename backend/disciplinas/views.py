from django.shortcuts import render

from .models import Disciplinas

def listar_disciplinas(request):
    disciplinas = Disciplinas.objects.all().values("nome", 'descricao')
    return JsonResponse(list(disciplinas), safe=False)