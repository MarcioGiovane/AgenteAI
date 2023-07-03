```python
from marshmallow import Schema, fields

class AlunoSchema(Schema):
    id = fields.Int(required=True)
    nome = fields.Str(required=True)
    idade = fields.Int(required=True)
    serie = fields.Str(required=True)

alunos = []

def adicionarAluno(id, nome, idade, serie):
    aluno = AlunoSchema().load({"id": id, "nome": nome, "idade": idade, "serie": serie})
    alunos.append(aluno)
    return {"message": "alunoAdicionado", "aluno": aluno}
```