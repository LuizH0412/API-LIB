# API de Gestão de Biblioteca

Esta é uma API desenvolvida para a gestão de uma biblioteca, utilizando Django REST Framework. A API fornece funcionalidades completas de CRUD e autenticação através de tokens utilizando o Simple JWT.

## Funcionalidades

- **CRUD Completo:** Permite operações de Create, Read, Update e Delete para as entidades principais da biblioteca.
- **Autenticação por Token:** Usa o Simple JWT para autenticação e autorização de usuários.
- **Endpoints:** A API está organizada em endpoints para gerenciar livros, empréstimos, autores e gêneros.

## Instalação

### Pré-requisitos

- Python 3.x
- Django
- Django REST Framework
- Django REST Framework Simple JWT

### Passos para Instalação

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Instale as Dependencias**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure o Banco de Dados**

    Edite o arquivo settings.py para configurar o banco de dados conforme necessário.

4. **Realize as Migrações**

    ```bash
    python manage.py migrate
    ```

5. **Crie um Superusuário**

    ```bash
    python manage.py createsuperuser
    ```

6. **Inicie o Servidor**

    ```bash
    python manage.py runserver
    ```

## Endpoints

Aqui estão alguns exemplos de endpoints disponíveis na API:

### Autenticação

- **Obter Token**
  
  **Método:** POST  
  **Endpoint:** `/api/v1/authentication/token/`  

  
  ```json
  {
    "username": "seu_usuario",
    "password": "sua_senha"
  }
  ```

### Livros

- **Listar Livros**
  
  **Método:** GET  
  **Endpoint:** `/api/v1/livros/`

- **Criar Livro**
  
  **Método:** POST  
  **Endpoint:** `/api/v1/livros/`  

  
  ```json
  {
    "titulo": "Título do Livro",
    "autor": "Autor do Livro",
    "genero": "Gênero do Livro",
    "ano_publicacao": 2024
  }
  ```

- **Atualizar Livro**
  
  **Método:** PUT  
  **Endpoint:** `/api/v1/livros/{id}/`  
  
  ```json
  {
    "titulo": "Novo Título",
    "autor": "Novo Autor",
    "genero": "Novo Gênero",
    "ano_publicacao": 2025
  }
  ```

- **Excluir Livro**

  **Método:** DELETE  
  **Endpoint:** `/api/v1/livros/{id}/`

### Empréstimos

- **Listar Empréstimos**

  **Método:** GET  
  **Endpoint:** `/api/v1/emprestimos/`


- **Criar Empréstimo**

  **Método:** POST  
  **Endpoint:** `/api/v1/emprestimos/`  
  
  ```json
  {
    "livro": 1,
    "usuario": 1,
    "data_emprestimo": "2024-08-01",
    "data_devolucao": "2024-09-01"
  }
  ```

### Atualizar Empréstimo

  **Método:** PUT  
  **Endpoint:** `/api/v1/emprestimos/{id}/`  

  ```json
  {
    "livro": 1,
    "usuario": 1,
    "data_emprestimo": "2024-08-01",
    "data_devolucao": "2024-09-10"
  }
  ```

### Excluir Empréstimo

**Método:** DELETE  
**Endpoint:** `/api/v1/emprestimos/{id}/`

### Autenticação

Para acessar os endpoints protegidos, você deve incluir um token de autenticação no cabeçalho das requisições.

**Exemplo de Cabeçalho com Token:**

```makefile
Authorization: Bearer seu_token_aqui
```

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Se você tiver sugestões, correções ou melhorias, por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License.