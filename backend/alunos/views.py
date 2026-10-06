from django.shortcuts import render

from .models import Alunos

def listar_alunos(request):
    alunos = Alunos.objects.all().values("nome", 'email', 'senha')
    return JsonResponse(list(alunos), safe=False)