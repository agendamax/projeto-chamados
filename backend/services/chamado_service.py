from datetime import datetime
from itertools import count
from schemas.chamado_schema import Chamado, ChamadoEntrada

chamados: dict[int, Chamado] = {}
proximo_id = count(1)


class ChamadoService:
    @staticmethod
    def criar_chamado(dados: ChamadoEntrada) -> Chamado:
        chamado_id = next(proximo_id)
        data_atual = datetime.now().isoformat()

        chamado = Chamado(
            id=chamado_id,
            criador=dados.criador,
            titulo=dados.titulo,
            descricao=dados.descricao,
            prioridade=dados.prioridade,
            status="aberto",
            data_criacao=data_atual,
        )
        chamados[chamado.id] = chamado
        return chamado

    @staticmethod
    def consultar_chamado(chamado_id: int) -> Chamado | None:
        return chamados.get(chamado_id)