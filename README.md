# API de Gestão de Biblioteca

Esta é uma API desenvolvida para a gestão de uma biblioteca, utilizando Django REST Framework. A API fornece funcionalidades completas de CRUD e autenticação através de tokens utilizando o Simple JWT.

## Funcionalidades

- **CRUD Completo:** Permite operações de Create, Read, Update e Delete para as entidades principais da biblioteca.
- **Autenticação por Token:** Usa o Simple JWT para autenticação e autorização de usuários.
- **Endpoints:** A API está organizada em endpoints para gerenciar livros, empréstimos, autores e gêneros.

## Boas Práticas

### Uso de Class-Based Views (CBVs) e ViewSets

Para manter o código organizado e eficiente, optamos por usar Class-Based Views (CBVs) e ViewSets na nossa API. Aqui estão algumas dicas sobre como e por que utilizamos essas ferramentas:

- **Class-Based Views (CBVs):** Utilizar CBVs nos permite uma abordagem mais modular e reutilizável ao criar views. Elas ajudam a manter o código mais limpo e estruturado, facilitando a manutenção e a extensão. Em vez de repetir código para operações básicas de CRUD, CBVs oferecem uma maneira mais elegante e coesa de gerenciar a lógica das views.

- **ViewSets:** ViewSets são uma excelente escolha para gerenciar operações CRUD de maneira eficiente. Eles agrupam as operações de listagem, detalhamento, criação, atualização e exclusão em uma única classe. Isso não só reduz a redundância no código, mas também garante que todas as operações relacionadas a um recurso sejam tratadas de forma consistente.

### Outras Boas Práticas

- **Serializers:** Usamos serializers para validar e transformar dados entre o formato JSON e os modelos do Django. Isso garante que os dados recebidos e enviados pela API estejam corretos e no formato esperado. Certifique-se de criar serializers específicos para cada modelo e de implementar validações personalizadas quando necessário.

- **Autenticação e Permissões:** É fundamental configurar corretamente a autenticação e as permissões para proteger a API. O Simple JWT é utilizado para autenticação por token, o que ajuda a controlar o acesso aos recursos de forma segura e eficiente.

- **Paginação:** Para endpoints que retornam grandes listas de dados, a paginação é uma prática importante. Ela melhora a performance da API e proporciona uma melhor experiência para os usuários ao lidar com grandes volumes de informações.


Seguindo essas boas práticas, garantimos que a API seja robusta, fácil de manter e capaz de crescer conforme necessário.

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
    "nome": "Título do Livro",
    "escritor": 1, 
    "genero": 1,
    "paginas": "000"
  }
  ```

- **Atualizar Livro**
  
  **Método:** PUT  
  **Endpoint:** `/api/v1/livros/{id}/`  
  
  ```json
  {
    "nome": "Título do Livro",
    "escritor": 1, 
    "genero": 1,
    "paginas": "000"
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
    "usuario": 1,
    "livro": 1,
    "usuario": 1,
    "data_devolucao": "2024-09-01",
    "status": "Pen" // Pendente (Pen) ; Devolvido (Dev)
  }
  ```

### Atualizar Empréstimo

  **Método:** PUT  
  **Endpoint:** `/api/v1/emprestimos/{id}/`  

  ```json
  {
    "usuario": 1,
    "livro": 1,
    "usuario": 1,
    "data_devolucao": "2024-09-01",
    "status": "Pen" // Pendente (Pen) ; Devolvido (Dev)
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

### Escritores

- **Listar Escritores**
  
  **Método:** GET  
  **Endpoint:** `/api/v1/escritores/`

- **Criar Escritor**
  
  **Método:** POST  
  **Endpoint:** `/api/v1/escritores/`  
  
  ```json
  {
    "nome": "Nome do Escritor",
    "nacionalidade": "Nacionalidade do Escritor",
    "data_nascimento": "YYYY-MM-DD",
    "data_falecimento": "YYYY-MM-DD",
    "idade": "00",
  }
  ```

- **Atualizar Escritor**
  
  **Método:** PUT  
  **Endpoint:** `/api/v1/escritores/{id}/` 
  
  ```json
  {
    "nome": "Nome do Escritor",
    "nacionalidade": "Nacionalidade do Escritor",
    "data_nascimento": "YYYY-MM-DD",
    "data_falecimento": "YYYY-MM-DD",
    "idade": "00",
  }
  ```


- **Atualizar Escritor**

    **Método:** PUT
    **Endpoint:** `/api/v1/escritores/{id}/`  

  ```json  
  {
    "nome": "Nome do Escritor",
    "nacionalidade": "Nacionalidade do Escritor",
    "data_nascimento": "YYYY-MM-DD",
    "data_falecimento": "YYYY-MM-DD",
    "idade": "00",
  }
  ```

- **Excluir Escritor**

    **Método:** DELETE
    **Endpoint:** `/api/v1/escritores/{id}/`


### Gêneros

- **Listar Gêneros**

    **Método:** GET
    **Endpoint:** `/api/v1/generos/`

- **Criar Gênero**
  
  **Método:** POST  
  **Endpoint:** `/api/v1/generos/`  
  
  ```json
  {
    "nome": "Nome do Gênero"
  }
  ```

**Atualizar Gênero**
  
  **Método:** PUT  
  **Endpoint:** `/api/v1/generos/{id}/`  

  ```json
  {
    "nome": "Novo Nome do Gênero"
  }
  ```

- **Excluir Gênero**
  
  **Método:** DELETE  
  **Endpoint:** `/api/v1/generos/{id}/`

### Usuários

- **Listar Usuários**
  
  **Método:** GET  
  **Endpoint:** `/api/v1/usuarios/`

- **Criar Usuário**
  
  **Método:** POST  
  **Endpoint:** `/api/v1/usuarios/`  
  **Payload:**
  
  ```json
  {
    "username": "nome_de_usuario",
    "first_name": "Primeiro Nome",
    "last_name": "Ultimo Nome",
    "password": "senha"
  }
  ```

- **Excluir Usuário**
  
  **Método:** DELETE  
  **Endpoint:** `/api/v1/usuarios/{id}/`

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Se você tiver sugestões, correções ou melhorias, por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License.