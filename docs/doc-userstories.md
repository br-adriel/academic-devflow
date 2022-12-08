# Documento Lista de User Stories

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos Funcionais no
[Documento de Visão](https://github.com/labens-ufrn/academic-devflow/blob/doc/issue2/docs/doc-visao.md).

## User Story US01 - Manter Usuário

|                              |                                                                                                                                                                                                                       |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**                | Um usuário tem username, password, tipo de usuário. Os usuários são criados automaticamente no cadastro de cada membro, mas o sistema deve permitir que cada usuário possa visualizar seus dados e também alterá-los. |                                                                         
| **Requisitos envolvidos**    | RF08                                                                                                                                                                                                                  |
| **Estimativa**               | 5 Horas                                                                                                                                                                                                              | 
| **Tempo Gasto (real):**      | ---                                                                                                                                                                                                                  |
| **Prioridades**              | Essencial                                                                                                                                                                                                            |
| **Tamanho Funcional**        | ---                                                                                                                                                                                                                  |
| **Analista**                 | Guilherme                                                                                                                                                                                                            |
| **Desenvolvedor**            | Não Definido                                                                                                                                                                                                          |
| **Revisor**                  | Não Definido                                                                                                                                                                                                          |
| **Testador**                 | Não Definido                                                                                                                                                                                                          |

## Teste de Aceitação

| **Código**  | **Descrição** |
|-------------|---------------|
| **TA01.01** | O usuário informa, na tela Registrar, todos os dados para registrar-se corretamente, ao clicar em Salvar ele é notificado com uma mensagem de sucesso. Mensagem: Cadastro realizado com sucesso, aguardando ativação do administrado |
| **TA01.02** | O usuário informa, na tela Registrar, os dados para registrar-se incorretamente, ao clicar em Salvar ele é notificado com uma mensagem de erro. Mensagem: Cadastro não realizado, o campo “xxxx” não foi informado corretamente. |
| **TA01.03** | O usuário informa, na tela Login, os dados para logar corretamente, ao clicar em Entrar ele é notificado com uma mensagem de erro. Mensagem: Usuário não ativado, aguardando ativação do administrador |
| **TA01.04** | O usuário informa, na tela Login, os dados para logar corretamente, ao clicar em Entrar ele é encaminhado para a tela principal do sistema. É exibida a Mensagem: Login realizado com sucesso. |
| **TA01.05** | No seu perfil, ao usuário clicar alterar, deverá ser capaz de alterar a informação desejada |
| **TA01.06** | No seu perfil, os campos que estão sendo alterados deverão ser atualizados corretamente, ao clicar em Salvar ele é notificado com uma mensagem de sucesso. Mensagem: Alteração realizada com sucesso. |
| **TA01.07** | O usuário informa, durante a alteração do perfil, os dados para registrar-se incorretamente, ao clicar em Salvar ele é notificado com uma mensagem de erro. Mensagem: Atualização não realizada, o campo “xxxx” não foi informado. |

## User Story US03 - Acessar Sistema

|                              |                                                                                                                                                                                                                       |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**                | Quando o usuário estiver adicionado suas credenciais, o sistema deverá permitir a liberação dos módulos de acesso, de acordo com a prioridade do usuário, isso irá liberar o acesso as funcionalidades dos componentes já implementados. |                                                                         
| **Requisitos envolvidos**    | RF03, RF04, RF09, RF10                                                                                                                                                                                                |
| **Estimativa**               | 10 Horas                                                                                                                                                                                                              | 
| **Tempo Gasto (real):**      | ---                                                                                                                                                                                                                  |
| **Prioridades**              | Essencial                                                                                                                                                                                                            |
| **Tamanho Funcional**        | ---                                                                                                                                                                                                                  |
| **Analista**                 | Hilário                                                                                                                                                                                                              |
| **Desenvolvedor**            | Não Definido                                                                                                                                                                                                          |
| **Revisor**                  | Não Definido                                                                                                                                                                                                          |
| **Testador**                 | Não Definido                                                                                                                                                                                                          |

## Teste de Aceitação

| **Código**  | **Descrição** |
|-------------|---------------|
| **TA03.01** | O usuário informa, na tela Login, os dados para logar corretamente, ao clicar em Entrar ele é encaminhado para a tela principal do sistema. É exibida a Mensagem: Login realizado com sucesso. |
| **TA03.02** | O usuário informa, na tela Login, os dados para logar incorretamente, ao clicar em Entrar ele é notificado com uma mensagem de erro. É exibida a Mensagem: Usuário não ativado, aguardando ativação do administrador. |
| **TA03.03** | No seu perfil, o usuário deverá ser capaz de visualizar todas as informações ao qual ele tem acesso. |
| **TA03.04** | No seu perfil, o usuário poderá listar informações desejadas e exportar os dados para um arquivo em formato de planilha, ao clicar em Exportar ele é notificado com uma mensagem de sucesso. É exibida a Mensagem: Lista "xxxx" exportada com sucesso. |

## User Story US02 - Manter projeto

|     |     |
| --- | --- |
| **Descrição** | O sistema deve permitir o cadastro, visualização, edição e exclusão de projetos. Membros podem apenas visualizar as informações dos projetos aos quais fazem parte. Coordenadores podem criar, visualizar e editar projetos que coordenam. Administradores podem realizar as quatro operações de forma irrestrita. Todas as operações demandam que o usuário esteja logado. |
| **Requisitos envolvidos** | RF01, RF02, RNF01, RNF02, RNF03 |
| **Prioridade** | Importante |
| **Estimativa** | 8h |
| **Tempo gasto (real)** | - |
| **Tamanho funcional** | 7PF (Pontos de função) |
| **Analista** | Adriel Faria dos Santos |
| **Desenvolvedor** | - |
| **Revisor** | - |
| **Testador** | - |

## Testes de aceitação (TA)

| Código | Descrição |
| ------ | --------- |
| TA02.01 | Um usuário não logado tenta visualizar um projeto cadastrado e não consegue, o sistema exibe a mensagem "Você precisa fazer login para visualizar projetos" |
| TA02.02 | Um usuário _Membro_ logado tenta visualizar um projeto do qual não faz parte e não consegue, o sistema exibe a mensagem "Você não possui permipermissão para visualizar esse projeto" |
| TA02.03 | Um usuário _Membro_ logado tenta visualizar um projeto do qual faz parte e consegue, o sistema exibe os dados referentes ao projeto |
| TA02.04 | Um usuário _Coordenador_ logado tenta visualizar um projeto do qual não faz parte e não consegue, o sistema exibe a mensagem "Você não possui permissão para visualizar esse projeto" |
| TA02.05 | Um usuário _Coordenador_ logado tenta visualizar um projeto do qual faz parte e consegue, o sistema exibe os dados referentes ao projeto |
| TA02.06 | Um usuário _Administrador_ logado tenta visualizar um projeto do qual não faz parte e consegue, o sistema exibe os dados referentes ao projeto |
| TA02.07 | Um usuário _Administrador_ logado tenta visualizar um projeto do qual faz parte e consegue, o sistema exibe os dados referentes ao projeto |
| TA02.08 | Um usuário não logado tenta cadastrar um projeto e não consegue, o sistema exibe a mensagem "Você precisa fazer login para cadastrar projetos" |
| TA02.09 | Um usuário _Membro_ logado tenta cadastrar um projeto e não consegue, o sistema exibe a mensagem "Você não possui permissão para cadastrar projetos" |
| TA02.10 | Um usuário _Coordenador_ logado tenta cadastrar um projeto e é direcionado para um formulário com os campos **Nome**, **Descrição** (opcional), **Situação**, **Data de início**, **Data de término**, **Equipe** e **Fluxo** |
| TA02.11 | Um usuário _Coordenador_ preenche o formulário de cadastro de projetos com todos os campos obrigatórios e o submete, o sistema salva o novo projeto e o redireciona para a página de visualização do projeto, que mostra os dados conforme foram preenchidos |
| TA02.12 | Um usuário _Coordenador_ preenche o formulário de cadastro de projetos com todos os campos obrigatórios e opcionais, e o submete, o sistema salva o novo projeto e o redireciona para a página de visualização, que mostra os dados conforme foram preenchidos |
| TA02.13 | Um usuário _Coordenador_ não preenche todos os campos obrigatórios do formulário de cadastro de projetos e o submete, o sistema exibe a mensagem de erro "Há campos obrigatórios não preenchidos" |
| TA02.14 | Um usuário _Administrador_ preenche o formulário de cadastro de projetos com todos os campos obrigatórios e o submete, o sistema salva o novo projeto e o redireciona para a página de visualização do projeto, que mostra os dados conforme foram preenchidos |
| TA02.15 | Um usuário _Administrador_ preenche o formulário de cadastro de projetos com todos os campos obrigatórios e opcionais, e o submete, o sistema salva o novo projeto e o redireciona para a página de visualização, que mostra os dados conforme foram preenchidos |
| TA02.16 | Um usuário _Administrador_ não preenche todos os campos obrigatórios do formulário de cadastro de projetos e o submete, o sistema exibe a mensagem de erro "Há campos obrigatórios não preenchidos" |
| TA02.17 | Um usuário não logado tenta editar um projeto e não consegue, o sistema exibe a mensagem "Você precisa fazer login para editar projetos" |
| TA02.18 | Um usuário _Membro_ logado tenta editar um projeto e não consegue, o sistema exibe a mensagem "Você não possui permissão para editar projetos" |
| TA02.19 | Um usuário _Coordenador_ logado tenta editar um projeto do qual não faz parte e não consegue, o sistema exibe a mensagem "Você não possui permissão para editar esse projeto" |
| TA02.20 | Um usuário _Coordenador_ logado tenta editar um projeto do qual faz parte e é direcionado para um formulário com os campos **Nome**, **Descrição** (opcional), **Situação**, **Data de início**, **Data de término**, **Equipe** e **Fluxo** preenchidos com os dados salvos no banco |
| TA02.21 | Um usuário _Coordenador_ preenche o formulário de edição de projeto, modificando todos os campos obrigatórios, deixando os campos opcionais em branco, e o submete, o sistema salva o projeto e o redireciona para a página de visualização, que mostra os dados conforme foram preenchidos e a mensagem "Alterações salvas" |
| TA02.22 | Um usuário _Coordenador_ preenche o formulário de edição de projeto, modificando todos os campos obrigatórios e opcionais, e o submete, o sistema salva o projeto e o redireciona para a página de visualização, que mostra os dados conforme foram preenchidos e a mensagem "Alterações salvas" |
| TA02.23 | Um usuário _Coordenador_ preenche o formulário de edição de projeto, deixando campos obrigatórios em branco, e o submete, o sistema exibe a mensagem "Há campos obrigatórios não preenchidos" |
| TA02.24 | Um usuário _Administrador_ logado tenta editar um projeto do qual não faz parte e consegue, o sistema o redireciona para um formulário com os campos **Nome**, **Descrição** (opcional), **Situação**, **Data de início**, **Data de término**, **Equipe** e **Fluxo** preenchidos com os dados salvos no banco |
| TA02.25 | Um usuário _Administrador_ logado tenta editar um projeto do qual faz parte e é direcionado para um formulário com os campos **Nome**, **Descrição** (opcional), **Situação**, **Data de início**, **Data de término**, **Equipe** e **Fluxo** preenchidos com os dados salvos no banco |
| TA02.26 | Um usuário _Administrador_ preenche o formulário de edição de projeto, modificando todos os campos obrigatórios, deixando os campos opcionais em branco, e o submete, o sistema salva o projeto e o redireciona para a página de visualização, que mostra os dados conforme foram preenchidos e a mensagem "Alterações salvas" |
| TA02.27 | Um usuário _Administrador_ preenche o formulário de edição de projeto, modificando todos os campos obrigatórios e opcionais, e o submete, o sistema salva o projeto e o redireciona para a página de visualização, que mostra os dados conforme foram preenchidos e a mensagem "Alterações salvas" |
| TA02.28 | Um usuário _Administrador_ preenche o formulário de edição de projeto, deixando campos obrigatórios em branco, e o submete, o sistema exibe a mensagem "Há campos obrigatórios não preenchidos" |
| TA02.29 | Um usuário não logado tenta excluir um projeto e não consegue, o sistema exibe a mensagem "Você precisa fazer login para excluir projetos" |
| TA02.30 | Um usuário _Membro_ logado tenta excluir um projeto e não consegue, o sistema exibe a mensagem "Você não possui permissão para excluir projetos" |
| TA02.31 | Um usuário _Coordenador_ logado tenta excluir um projeto e não consegue, o sistema exibe a mensagem "Você não possui permissão para excluir projetos" |
| TA02.32 | Um usuário _Administrador_ logado tenta excluir um projeto e o sistema exibe um forulário com botões para confirmar ou cancelar a operação, o usuário confirma a operação, o sistema exclui o registro, o redireciona para a página inicial e exibe a mensagem "Projeto excluido" |
| TA02.33 | Um usuário _Administrador_ logado tenta excluir um projeto e o sistema exibe um forulário com botões para confirmar ou cancelar a operação, o usuário cancela a operação e o sistema mantém o registro |

## User Story US03 - Manter Fluxo de desenvolvimento

|           |           |
| --------- | --------- |
| **Descrição:** | Um fluxo de desenvolvimento tem código, nome, descrição, quantidade de etapas. O sistema deve permitir o cadastro de um novo fluxo de desenvolvimento para cada projeto, assim como a alteração e visualização deste. |
| **Requisitos Envolvidos** | RF03 | Manter Fluxo de desenvolvimento |
| **Prioridade**            | Essencial |
| **Estimativa**            | 8h |
| **Tempo Gasto (real):**   | --- |
| **Tamanho Funcional**     | --- |
| **Analista**              | Hil (responsável por especificar/detalhar o US) |
| **Desenvolvedor**         | Adriel (responsável por implementar e realizar testes de unidade e testes de integração) |
| **Revisor**               | Guilherme (responsável por avaliar a implementação e executar os testes de unidade e testes de integração) |
| **Testador**              | Guilherme (responsável por executar os Testes de Aceitação e fazer o relatório de testes) |

## **Testes de Aceitação (TA)**

| **Código**  | **Descrição** |     
| ----------- | ------------- |
| **TA03.01** | O usuário deseja cadastrar um novo fluxo de desenvolvimento, então o usuário clica no botão inserir fluxo de desenvolvimento. O usuário preenche todos os campos de modo correto e clica em Salvar/Cadastrar, recebendo uma notificação em tela de sucesso, como "Fluxo de desenvolvimento cadastrado com sucesso". |
| **TA03.02** | O usuário deseja cadastrar um novo fluxo de desenvolvimento, então o usuário clica no botão inserir fluxo de desenvolvimento. O usuário preenche algum campo ou todos os campos de modo incorreto e clica em Salvar/Cadastrar, o usuário é notificado com uma mensagem de erro. Mensagem: Cadastro não realizado, o campo “xxxx” não foi informado corretamente. |
| **TA03.03** | O usuário deseja alterar o fluxo de desenvolvimento, então o usuário clica no botão editar fluxo de desenvolvimento. O usuário altera os campos que deseja de modo correto e clica em Editar/Salvar, recebendo uma notificação em tela de sucesso, como "Fluxo de desenvolvimento alterado com sucesso". |                                                     
| **TA03.04** | O usuário deseja alterar o fluxo de desenvolvimento, então o usuário clica no botão editar fluxo de desenvolvimento. O usuário altera algum campo ou todos os campos de modo incorreto e clica em Editar/Salvar, o usuário é notificado com uma mensagem de erro. Mensagem: A operação falhou, o campo “xxxx” não foi informado corretamente. | 
| **TA03.05** | O usuário deseja excluir o fluxo de desenvolvimento, o usuário clica no botão excluir, caso o fluxo de desenvolvimento já possua etapas cadastradas, o sistema deve informar ao usuário e perguntar se realmente deseja excluir o fluxo de desenvolvimento, caso o usuário confirme, o sistema envia o fluxo para a lixeria e notifica ao usuário com uma mensagem de sucesso. Mensagem: "Fluxo de desenvolvimento excluído com sucesso".   Caso o usuário não confirme, ele deve ser notificado com uma mensagem informando que nenhuma mudança ocorreu. |          

