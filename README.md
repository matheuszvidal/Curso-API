# Projeto CursoAPI - Documentação do Desenvolvedor
Bem-vindo ao Projeto **CursoAPI!** Esta documentação fornece informações essenciais para desenvolvedores que estão se familiarizando com o projeto. Aqui, você encontrará uma visão geral do projeto, instruções sobre como executá-lo localmente e uma descrição das principais rotas da API.

## 1. Apresentação do Projeto
O Projeto **CursoAPI** é uma aplicação que gerencia cursos, oferecendo funcionalidades básicas de criação, leitura, atualização e exclusão (CRUD). Utilizando as tecnologias **FastAPI**, **SQLite** e **Uvicorn**, o projeto proporciona uma API robusta e eficiente para gerenciar dados de cursos.

- **Tecnologias Utilizadas:**
    - **FastAPI:** Um framework web rápido, moderno e fácil de usar para Python, que utiliza tipagem de dados para aumentar a segurança e a eficiência no desenvolvimento de APIs.
    - **SQLite:** Um sistema de gerenciamento de banco de dados leve e amplamente utilizado, perfeito para projetos de pequeno a médio porte.
    - **Uvicorn:** Um servidor ASGI rápido que facilita a execução de aplicações FastAPI.

- **Observação do Desenvolvedor:**
Este é meu primeiro projeto utilizando FastAPI, e como tal, algumas convenções e nomenclaturas podem não seguir padrões estabelecidos. Agradeço pela compreensão e estou aberto a feedback e sugestões para a melhoria contínua do projeto.

## 2. Como Rodar Localmente

Siga as etapas abaixo para configurar e executar o projeto em seu ambiente local:

### 2.1 Pré-requisitos

- Python (versão recomendada 3.6 ou superior)
- Uvicorn
- Pip (instalador de pacotes Python)

### 2.2 Criar e Ativar o Ambiente Virtual

1. Abra um terminal ou prompt de comando no diretório raiz do projeto.

2. Execute o seguinte comando para criar um ambiente virtual chamado `.venv`:

    ```bash
    python -m venv .venv
    ```

3. Ative o ambiente virtual:

   - **No Linux/Mac:**

      ```bash
      source .venv/bin/activate
      ```

   - **No Windows (PowerShell):**

      ```powershell
      .\.venv\Scripts\Activate
      ```

   - **No Windows (Command Prompt):**

      ```cmd
      .venv\Scripts\activate
      ```

4. Com o ambiente virtual ativado, continue com as etapas para instalar as dependências e iniciar o servidor local.

### 2.3 Instalação de Dependências

1. Execute o seguinte comando para instalar as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

### 2.4 Iniciando o Servidor Local

1. Com as dependências instaladas, execute o seguinte comando no terminal para iniciar o servidor Uvicorn:

    ```bash
    uvicorn app:app --reload
    ```
### 2.5 Acessando a Documentação da API
- Documentação Swagger: http://127.0.0.1:8000/docs
- Documentação Redoc: http://127.0.0.1:8000/redoc

Esses links fornecem interfaces interativas para explorar, entender e testar as principais funcionalidades da API.

## 3. Principais Rotas da API

### 3.1 Listar Todos os Cursos

- **Endpoint:** `GET /api/cursos`
- **Descrição:** Obtém a lista de todos os cursos disponíveis.
- **Parâmetros:** Nenhum.
- **Resposta Bem-sucedida (200):**
  - Tipo de Mídia: `application/json`
  - Exemplo de Valor:
    ```json
    [
      {
        "titulo": "string",
        "descricao": "string",
        "carga_horaria": 0,
        "qtd_exercicios": 0,
        "id": 0
      }
    ]
    ```

### 3.2 Criar um Novo Curso

- **Endpoint:** `POST /api/cursos`
- **Descrição:** Cria um novo curso.
- **Parâmetros:** Nenhum.
- **Corpo da Solicitação (JSON):**
  ```json
  {
    "titulo": "string",
    "descricao": "string",
    "carga_horaria": 0,
    "qtd_exercicios": 0
  }
  ```
- **Resposta Bem-sucedida (201):**
  - Tipo de Mídia: `application/json`
  - Exemplo de Valor:
    ```json
    {
      "titulo": "string",
      "descricao": "string",
      "carga_horaria": 0,
      "qtd_exercicios": 0,
      "id": 0
    }
    ```

### 3.3 Obter Detalhes de um Curso por ID

- **Endpoint:** `GET /api/cursos/{id}`
- **Descrição:** Obtém detalhes de um curso específico com base no ID.
- **Parâmetros:**
  - **id***: integer (path)
- **Resposta Bem-sucedida (200):**
  - Tipo de Mídia: `application/json`
  - Exemplo de Valor:
    ```json
    {
      "titulo": "string",
      "descricao": "string",
      "carga_horaria": 0,
      "qtd_exercicios": 0,
      "id": 0
    }
    ```

### 3.4 Atualizar Detalhes de um Curso por ID

- **Endpoint:** `PUT /api/cursos/{id}`
- **Descrição:** Atualiza os detalhes de um curso específico com base no ID.
- **Parâmetros:**
  - **id***: integer (path)
- **Corpo da Solicitação (JSON):**
  ```json
  {
    "titulo": "string",
    "descricao": "string",
    "carga_horaria": 0,
    "qtd_exercicios": 0
  }
  ```
- **Resposta Bem-sucedida (200):**
  - Tipo de Mídia: `application/json`
  - Exemplo de Valor:
    ```json
    {
      "titulo": "string",
      "descricao": "string",
      "carga_horaria": 0,
      "qtd_exercicios": 0,
      "id": 0
    }
    ```

### 3.5 Excluir um Curso por ID

- **Endpoint:** `DELETE /api/cursos/{id}`
- **Descrição:** Exclui um curso específico com base no ID.
- **Parâmetros:**
  - **id***: integer (path)
- **Resposta Bem-sucedida (204):**
  - Sem links.

## 4. Equipe de Desenvolvimento

### Autor
- **Nome do Autor:** Matheus Vidal
- **Cargo:** Desenvolvedor Full Stack
- **E-mail:** matheusvidalpro@gmail.com
- **Perfil GitHub:** github.com/matheuszvidal
