# Documento de Visão 

## Equipe e Definição de Papéis

| Membro                       | Papel                             | E-mail                         |
| ---------------------------- | --------------------------------- | ------------------------------ |
| Taciano de Morais Silva      | Cliente                           | taciano.silva@ufrn.br          |
| Adriel Faria dos Santos      | Desenvolvedor, Testador           | adriel.fsantos@outlook.com     |
| Guilherme Angelo de Medeiros | Desenvolvedor, Testador           | guilhermeangelo2001@gmail.com  |
| Hilário Petronio D.M Dantas  | Desenvolvedor, Testador           | hilariod94@gmail.com           |

## Matriz de Competências 

| Equipe                       | Competências 
| ---------------------------- | -----------
| Adriel Faria dos Santos      | à definir
| Guilherme Angelo de Medeiros | à definir
| Hilário Petronio D.M Dantas  | à definir


## Descrição do Projeto 

Sistema para facilitar o acompanhamento do andamento de Projetos de Software dos discentes nas turmas de Engenharia de Software do curso de Bacharelado em Sistemas de Informação do CERES/UFRN. O sistema deve oferecer funcionalidades de gerenciamento de usuários, sejam eles tanto professores quanto alunos, projetos, fluxos, etapas, equipe, atividades e artefatos. O sistema também deve ser capaz de pontuar as atividades e artefatos ligados a um projeto, além disso, deve possuir uma integração com github sendo capaz de acompanhar commits quando realizados pelos membros de um projeto.

## Perfis dos Usuários

O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:

- Perfil Administrador 

Este usuário tem acesso a todas as entidades e funcionalidades do sistema, além de ter acesso à base de dados. Além de visualizar relatórios. 

- Perfil Aluno

Este usuário utiliza o sistema para realizar o gerenciamento do projeto ao qual ele faz parte, e também dos artefatos ligados ao projeto.

- Perfil Professor 

Este usuário utiliza o sistema para realizar o cadastro e gerenciamento dos projetos que coordena e também da equipe de projeto. Além disso, este usuário pode visualizar todos os artefatos produzidos ao longo do fluxo de desenvolvimento e gerar relatórios ao fim e cada iteração. 

## Requisitos funcionais 

Requisito | Título | Descrição | Ator
--------- | ------ | --------- | ----
| RF01 | Acessar sistema | O sistema deve possuir um módulo de autenticação e autorização para seu uso. Usuários que já possuem contas, devem informar suas credencias (usuário e senha) para acessar o sistema. Para os usuários que ainda não possuem conta, devem preencher um formulário de cadastro, contendo os campos: nome, e-mail e telefone. Após o preenchimento do formulário, o usuário deve aceitar os termos de uso e política de privacidade. | Professor. |
| RF02 | Manter Projeto | Um projeto tem código, nome, descrição, situação, data de início, data prevista de término, coordenador, equipe, fluxo de desenvolvimento. O sistema deve permitir o cadastro de um novo projeto, assim como a alteração e visualização deste. Observação: Para se criar um projeto, o usuário deve possuir uma conta. | Professor. |
| RF03 | Manter Fluxo de desenvolvimento | Um fluxo de desenvolvimento tem código, nome, descrição, quantidade de etapas. O sistema deve permitir o cadastro de um novo fluxo de desenvolvimento para cada projeto, assim como a alteração e visualização deste. | Professor. |
| RF04 | Manter Etapa | Uma etapa tem código, nome, descrição, data de início, data de finalização, pontuação. No momento de cadastro do fluxo de desenvolvimento, o sistema deve permitir o cadastro das etapas do processo de desenvolvimento, assim como a alteração, visualização e exclusão destas etapas. | Professor. |
| RF05 | Manter Coordenador | Um coordenador tem código, nome, e-mail, telefone, usuário. O sistema deve oferecer a opção de cadastrar um novo coordenador ou vários coordenadores, assim como a alteração e visualização deste(s). | Professor. | 
| RF06 | Manter Equipe | Uma equipe tem código, nome, quantidade de membros, coordenador. O sistema deve permitir o cadastro da equipe responsável pelo projeto, assim como a alteração, visualização e exclusão da equipe. | Professor. | 
| RF07 | Manter Membro | Um membro tem código, nome, e-mail, telefone, função, equipe, usuário, coordenador. No momento de cadastro de cada membro da equipe, deve ser criado automaticamente um usuário de acesso para aquele membro e deve ser enviado um e-mail contendo o usuário de acesso e uma senha temporária. | Professor. | 
| RF08 | Manter Usuário | Um usuário tem username, password, tipo de usuário. Os usuários são criados automaticamente no cadastro de cada membro, mas o sistema deve permitir que cada usuário possa visualizar seus dados e também alterá-los. | Aluno/Professor.|
| RF09 | Manter Artefato | Um artefato tem código, nome, descrição, situação, data de entrega, etapa, pontuação, projeto. O sistema deve permitir o cadastro de artefatos para cada etapa do fluxo de desenvolvimento, assim como a alteração, visualização, exclusão e listagem dos artefatos. | Professor/Aluno. |
| RF10 | Manter Atividade | Uma atividade tem código, nome, descrição, situação, data de início, data de conclusão, projeto, responsável. O sistema deve permitir o cadastro de atividades para o projeto, assim como a alteração, visualização e exclusão destas. | Professor/Aluno. | 
| RF11 | Manter Plano de Iteração e Plano de Release | O sistema deve permitir o cadastro do plano de iteração e plano de release, assim como a visualização, alteração e exclusão. | Aluno/Professor. |
| RF12 | Integração com o GitHub | O sistema deve permitir realizar a integração do projeto com o repositório do GitHub que contém o código desenvolvimento ao longo do fluxo de desenvolvimento. | Professor. |
| RF13 | Integração com o APF | O sistema deve permitir realizar a integração do projeto com o software de Análise de Ponto de Função. | Professor. |
| RF14 | Integração com o sistema da Monitoria do BSI | O sistema deve permitir a integração com o Sistema da Monitoria do BSI | Professor. |
| RF15 | Emissão de relatórios | O sistema deve ser capaz de criar relatórios acerca do desempenho da equipe como um todo e também de cada membro. | Professor/Aluno. |
| RF16 | Dashboard de métricas | O sistema deve criar um dashboard com gráficos e figuras com base nas métricas estabelicidas dentro do projeto. | Professor/Aluno. |
| RF17 | Envio de notificações | O sistema deve possuir um módulo de notificações, de modo que seja possível que o usuário seja notificado quando o prazo de uma tarefa estiver chegando ao fim; quando uma tarefa for atribuída a ele; entre outros exemplos. | --- |
| RF18 | Cadastro de pontuação | O sistema deve permitir que o coordenador atribua pontuações para cada etapa do projeto, assim como para os artefatos. | Professor. |
| RF19 | Cadastro de penalidades | O sistema deve permitir que o coordenador atribua penalidades para atrasos de tarefas ou não entrega de artefatos. | Professor. |

## Requisitos não funcionais

| Requisito | Descrição |
| --------- | --------- |
| RNF01     | O sistema deve ser acessível via navegador
| RNF02     | O sistema deve rodar em Windows e Linux
| RNF03     | O sistema deve ser feito o log de ações dos usuários
| RNF04     | O sistema deve possuir alta disponibilidade
| RNF05     | O sistema deverá atender as normas legais
| RNF05     | Os dados dos clientes devem ser de cunho privado


## Riscos

| Data       | Risco                                                                 | Prioridade | Responsável               | Status                  | Providência Solução                                                                     |
|------------|-----------------------------------------------------------------------|------------|---------------------------|-------------------------|-----------------------------------------------------------------------------------------|
| 03/09/2022 | Não aprendizado das ferramentas utilizadas pelos componentes do grupo | Alta       | Gerente                   | vigente                 | Reforçar estudos sobre as ferramentas e aulas com a integrante que conhece a ferramenta |
| 03/09/2022 | Ausência por qualquer motivo do cliente                               | Média      | Gerente                   | vigente                 | Planejar o cronograma tendo em base a agenda do cliente                                 |
| 03/09/2022 | Divisão de tarefas mal sucedida                                       | Baixa      | Gerente                   | Resovido                | Acompanhar de perto o desenvolvimento de cada membro da equipe                          |
| 03/09/2022 | Implementação de protótipo com as tecnologias                         | Alta       | Todos                     | vigente                 | Encontrar tutorial com a maioria da tecnologia e implementar um caso base do sistema    |
| 03/09/2022 | Ausência de um plano de testes                                        | Alta       | Todos                     | vigente                 | Entrar em contato com o testador(es) responsáveis e solicitar o planejamento            |
| 03/09/2022 | Falta de comunicação entre os envolvidos do projeto                   | Alta       | Todos                     | vigente                 | Os envolvidos devem comunicar-se através dos grupos e ferramentas definidas             |
| 03/09/2022 | Tecnologias não definidas                                             | baixa      | Gerente                   | vigente                 | O gerente deve definir quais tecnologias e ferramentas serão utilizadas                 |
| 03/09/2022 | Ausência de trabalho em equipe                                       | baixa      | Todos                     | vigente                 | A equipe deve ajudar-se independentimente do nível de experiência de cada desenvolvedor |
