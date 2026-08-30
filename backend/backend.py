from itertools import count

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI(title="API de Chamados")


class ChamadoEntrada(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    prioridade: str | None = None


class Chamado(BaseModel):
    id: int
    titulo: str
    descricao: str
    prioridade: str
    status: str


chamados: dict[int, Chamado] = {}
proximo_id = count(1)


def resposta_dado_invalido(campos: list[str]) -> JSONResponse:
    """Mantém o formato de erro definido no contrato da API."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "erro": "Dado inválido",
            "detalhes": [
                {"campo": campo, "mensagem": f"O campo {campo} é obrigatório."}
                for campo in campos
            ],
        },
    )


@app.post("/chamados", response_model=Chamado, status_code=status.HTTP_201_CREATED)
def criar_chamado(dados: ChamadoEntrada):
    obrigatorios = ["titulo", "descricao", "prioridade"]
    ausentes = [campo for campo in obrigatorios if not getattr(dados, campo)]

    if ausentes:
        return resposta_dado_invalido(ausentes)

    chamado = Chamado(
        id=next(proximo_id),
        titulo=dados.titulo,
        descricao=dados.descricao,
        prioridade=dados.prioridade,
        status="aberto",
    )
    chamados[chamado.id] = chamado

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=chamado.model_dump(),
        headers={"Location": f"/chamados/{chamado.id}"},
    )


@app.get("/chamados/{chamado_id}", response_model=Chamado)
def consultar_chamado(chamado_id: int):
    chamado = chamados.get(chamado_id)

    if chamado is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "erro": "Recurso inexistente",
                "detalhes": [
                    {"mensagem": f"Chamado com id {chamado_id} não foi encontrado."}
                ],
            },
        )

    return chamado
