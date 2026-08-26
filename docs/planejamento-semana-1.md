# Planejamento Inicial — Sistema de Chamados

`1. Descrição do problema e do domínio`

## Descrição

A empresa de suporte tecnico enfrenta dificuldades para controlar suas solicitações, pois atualmente utiliza planilhas e mensagens dispersas, o que dificulta localizar chamados, acompanhar seus atendimentos e manter um historico confiável. A nova aplicação devera centralizar o registro e o acompanhamento dos chamados, permitindo que clientes registrem solicitações e acompanhem seu andamento, enquanto a equipe de suporte podera consultar, atualizar e encerrar os chamados. O sistema sera direcionado ao dominio de suporte tecnico e gestão de chamados.

`2. Escopo inicial e pessoas usuarias`

## Funcionalidades incluidas

A primeira versão do sistema terá como objetivo atender às operações básicas de gestão de chamados.

- registro de chamados
- consulta de chamados
- atualizar chamados
- excluir chamados

## Evolução futura

Em uma evolução futura, o sistema podera enviar notificações para a pessoa cliente quando houver alteração no status de seu chamado. e a pessoa atendente podera filtrar por chamados.

## Pessoas usuarias

| Pessoa usuária    | Objetivo principal                                  |
| ----------------- | --------------------------------------------------- |
| Pessoa cliente:   | Registrar, editar, excluir e acompanhar um chamado. |
| Pessoa atendente: | Consultar, atualizar chamados.                      |

`3. Requisitos funcionais e recursos`

## Requisitos Funcionais

**[RF001]** O sistema deve permitir que o usuário crie chamados.

**[RF002]** O sistema deve permitir que o usuário edite chamados.

**[RF003]** O sistema deve permitir que o usuário exclua um chamado (criado por ele).

**[RF004]** O sistema deve permitir que o usuário visualize o status do chamado.

**[RF005]** O sistema deve permitir que o usuário consulte um chamado.

**[RF006]** O sistema deve permitir que o usário atualize o status de um chamado.

## Recursos

| Recursos  | Possíveis informações                                |
| --------- | ---------------------------------------------------- |
| Chamados  | ID, Nome do criador, Titulo, Descrição, Status, Data |
| Cliente   | ID, Nome, Email                                      |
| Atendente | ID, Nome                                             |

`4. Descrição do fluxo prioritario`

## Fluxo prioritário — Registrar chamado

1. A pessoa cliente acessa a tela de abertura de chamado.
2. A pessoa cliente informa os dados solicitados, como título e descrição do problema.
3. A interface web envia as informações preenchidas para a API.
4. O back-end recebe a solicitação, valida os dados e cria o chamado.
5. O banco de dados armazena as informações do chamado.
6. A aplicação retorna a confirmação do registro para a interface.
7. A interface informa à pessoa cliente que o chamado foi registrado com sucesso.