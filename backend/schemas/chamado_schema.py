from pydantic import BaseModel


class ChamadoEntrada(BaseModel):
    criador: str | None = None
    titulo: str | None = None
    descricao: str | None = None
    prioridade: str | None = None


class Chamado(BaseModel):
    id: int
    criador: str
    titulo: str
    descricao: str
    prioridade: str
    status: str
    data_criacao: str