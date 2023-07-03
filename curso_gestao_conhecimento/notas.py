```python
from marshmallow import Schema, fields

class NotaSchema(Schema):
    aluno_id = fields.Int(required=True)
    nota = fields.Float(required=True)
    materia = fields.Str(required=True)

notas = []

def atualizarNota(aluno_id, nota, materia):
    for n in notas:
        if n['aluno_id'] == aluno_id and n['materia'] == materia:
            n['nota'] = nota
            print('notaAtualizada')
            return
    notas.append({'aluno_id': aluno_id, 'nota': nota, 'materia': materia})
    print('notaAtualizada')

def getNota(aluno_id, materia):
    for n in notas:
        if n['aluno_id'] == aluno_id and n['materia'] == materia:
            return n['nota']
    return None
```