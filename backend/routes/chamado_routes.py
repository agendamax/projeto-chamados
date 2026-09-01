from fastapi import APIRouter, status
from schemas.chamado_schema import Chamado, ChamadoEntrada
from controllers.chamado_controller import ChamadoController

router = APIRouter(prefix="/chamados", tags=["Chamados"])


@router.post("", response_model=Chamado, status_code=status.HTTP_201_CREATED)
def criar_chamado(dados: ChamadoEntrada):
    return ChamadoController.handle_criar(dados)


@router.get("/{chamado_id}", response_model=Chamado)
def consultar_chamado(chamado_id: int):
    return ChamadoController.handle_consultar(chamado_id)