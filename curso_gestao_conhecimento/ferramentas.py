```python
# Importing required modules
import random

# Shared variables
from alunos import alunos
from notas import notas

# Function to use a tool
def usarFerramenta(ferramenta):
    if ferramenta == "flashcards":
        return aplicarFlashcards()
    elif ferramenta == "resumos":
        return aplicarResumos()
    elif ferramenta == "testes":
        return aplicarTestes()
    else:
        return "Ferramenta não reconhecida"

# Function to apply flashcards
def aplicarFlashcards():
    for aluno in alunos:
        flashcards = criarFlashcards(aluno)
        aluno['flashcards'] = flashcards
    return "Flashcards aplicados com sucesso"

# Function to create flashcards
def criarFlashcards(aluno):
    flashcards = []
    for nota in notas:
        if nota['aluno_id'] == aluno['id']:
            flashcard = {
                'pergunta': nota['materia'],
                'resposta': nota['conteudo']
            }
            flashcards.append(flashcard)
    return flashcards

# Function to apply summaries
def aplicarResumos():
    for aluno in alunos:
        resumo = criarResumo(aluno)
        aluno['resumo'] = resumo
    return "Resumos aplicados com sucesso"

# Function to create summaries
def criarResumo(aluno):
    resumo = []
    for nota in notas:
        if nota['aluno_id'] == aluno['id']:
            resumo_item = {
                'materia': nota['materia'],
                'resumo': nota['conteudo'][:100]  # First 100 characters
            }
            resumo.append(resumo_item)
    return resumo

# Function to apply tests
def aplicarTestes():
    for aluno in alunos:
        teste = criarTeste(aluno)
        aluno['teste'] = teste
    return "Testes aplicados com sucesso"

# Function to create tests
def criarTeste(aluno):
    teste = []
    for nota in notas:
        if nota['aluno_id'] == aluno['id']:
            teste_item = {
                'materia': nota['materia'],
                'pergunta': nota['conteudo'],
                'resposta': random.choice(['A', 'B', 'C', 'D'])  # Random answer
            }
            teste.append(teste_item)
    return teste
```