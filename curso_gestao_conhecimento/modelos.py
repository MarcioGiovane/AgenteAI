```python
from marshmallow import Schema, fields

class AlunoSchema(Schema):
    id = fields.Int(required=True)
    nome = fields.Str(required=True)
    idade = fields.Int(required=True)
    notas = fields.List(fields.Float(), required=True)

class NotaSchema(Schema):
    id_aluno = fields.Int(required=True)
    nota = fields.Float(required=True)
    materia = fields.Str(required=True)

class CursoSchema(Schema):
    id = fields.Int(required=True)
    nome = fields.Str(required=True)
    descricao = fields.Str(required=True)
    alunos = fields.Nested(AlunoSchema, many=True)

def aplicarModelo(curso, modelo):
    curso = CursoSchema().load(curso)
    for aluno in curso['alunos']:
        aluno = AlunoSchema().load(aluno)
        notas = aluno['notas']
        notas_modelo = modelo(notas)
        aluno['notas'] = notas_modelo
    return CursoSchema().dump(curso)
```