# Contrato Inicial - API de chamados

## Recurso

- Nome: `chamados`
- Finalidade: Um chamado registra uma solicitação de suporte enviada por uma pessoa usuária para resolução de um problema ou dúvida.

## Forma de dados

- Requisições e respostas: JSON

## Atributos

| Campo           | Tipo Sugerido | Obrigatório na Criação? | Exemplo                                                              | Observação                                                              |
| --------------- | ------------- | ----------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| ID              | Inteiro       | Não                     | 12                                                                   | Gerado automaticamente.                                                 |
| Nome do criador | Texto         | Sim                     | "João Alberto"                                                       | Nome do responsavel pela criação do chamado.                            |
| Titulo          | Texto         | Sim                     | "Erro ao enviar"                                                     | Titulo do problema.                                                     |
| Descrição       | Texto         | Sim                     | "Ao clicar no botão 'enviar' no envio de um pedido, ocorre um erro." | Descrição breve do problema.                                            |
| Status          | Texto         | Não                     | "Aberto"                                                             | Preenchido automaticamente pelo sistema como "Aberto" assim que criado. |
| Data            | Data/Hora     | Não                     | "2026-08-27 10:30:00"                                                | Gerado automaticamente no envio do chamado.                             |
