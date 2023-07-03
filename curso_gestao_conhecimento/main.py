```python
from metodologia import aplicarMetodologia
from ferramentas import usarFerramenta
from modelos import aplicarModelo
from hacks import usarHack
from estudo_minimo import estudarMinimo
from alunos import adicionarAluno
from notas import atualizarNota

curso = {
    "nome": "Gestão do conhecimento aplicado a aprendizado acelarado",
    "publico_alvo": "alunos do ensino médio do Brasil",
    "objetivo": "tornar os alunos os melhores, mesmo que tirem péssimas notas",
    "metodologia": [],
    "ferramentas": [],
    "modelos": [],
    "hacks": [],
}

alunos = []
notas = {}

def criarCurso():
    curso['metodologia'] = aplicarMetodologia()
    curso['ferramentas'] = usarFerramenta()
    curso['modelos'] = aplicarModelo()
    curso['hacks'] = usarHack()

def main():
    criarCurso()
    while True:
        aluno = adicionarAluno()
        if not aluno:
            break
        alunos.append(aluno)
        notas[aluno] = estudarMinimo(curso, aluno)
        atualizarNota(aluno, notas[aluno])

if __name__ == "__main__":
    main()
```