```python
# Importing required modules
from curso_gestao_conhecimento.alunos import alunos
from curso_gestao_conhecimento.notas import notas

def usarHack(aluno_id, hack_id):
    """
    Function to apply a hack to a student's study method.
    """
    try:
        aluno = next(aluno for aluno in alunos if aluno['id'] == aluno_id)
    except StopIteration:
        return "Aluno não encontrado."

    try:
        hack = next(hack for hack in hacks if hack['id'] == hack_id)
    except StopIteration:
        return "Hack não encontrado."

    # Apply the hack
    aluno['metodo_estudo'] = hack['metodo']
    return "Hack aplicado com sucesso."

hacks = [
    {
        'id': 1,
        'nome': 'Hack de Estudo Acelerado',
        'metodo': 'Estudo em blocos de 25 minutos com intervalos de 5 minutos.'
    },
    {
        'id': 2,
        'nome': 'Hack de Memorização',
        'metodo': 'Técnica de loci para memorização de conteúdo.'
    },
    {
        'id': 3,
        'nome': 'Hack de Leitura Dinâmica',
        'metodo': 'Leitura dinâmica para absorção rápida de conteúdo.'
    }
]
```