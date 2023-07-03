```python
from alunos import alunos
from notas import notas

def estudarMinimo():
    for aluno in alunos:
        nota_minima = min(notas[aluno])
        if nota_minima < 7:
            print(f"Aluno {aluno} precisa estudar mais!")
        else:
            print(f"Aluno {aluno} está indo bem, mas pode melhorar estudando menos!")

if __name__ == "__main__":
    estudarMinimo()
```