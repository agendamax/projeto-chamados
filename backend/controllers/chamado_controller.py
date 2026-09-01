from fastapi import status
from fastapi.responses import JSONResponse
from schemas.chamado_schema import ChamadoEntrada
from services.chamado_service import ChamadoService


class ChamadoController:
    @staticmethod
    def _resposta_dado_invalido(campos: list[str]) -> JSONResponse:
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

    @classmethod
    def handle_criar(cls, dados: ChamadoEntrada):
        obrigatorios = ["criador", "titulo", "descricao", "prioridade"]
        ausentes = [campo for campo in obrigatorios if not getattr(dados, campo)]

        if ausentes:
            return cls._resposta_dado_invalido(ausentes)

        chamado = ChamadoService.criar_chamado(dados)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=chamado.model_dump(),
            headers={"Location": f"/chamados/{chamado.id}"},
        )

    @classmethod
    def handle_consultar(cls, chamado_id: int):
        chamado = ChamadoService.consultar_chamado(chamado_id)

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