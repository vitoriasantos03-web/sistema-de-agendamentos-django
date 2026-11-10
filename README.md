# Sistema de Agendamentos
[Explique em 1 ou 2 frases o que o sistema faz. Ex: Sistema web para agendar atendimentos, que impede dois clientes no mesmo dia e horário.]
## Tecnologias
- Python
- Django
- SQLite
  ## Funcionalidades
  - Cadastro de agendamentos (nome do cliente, data, horário e serviço)
  - Bloqueio de agendamentos duplicados no mesmo dia e horário
  - Painel administrativo do Django
    ## Como rodar
    1. Clone o repositório
    2. Crie e ative o ambiente virtual:
    py -m venv venv
    venv\Scripts\activate
    3. Instale o Django:
    pip install django
    4. Crie o banco de dados:
    py manage.py migrate
    5. Crie um usuário administrador:
    py manage.py creatsuperuser
    6. Rode o servidor:
    py manage.py runserver
    7. Acesse http://127.0.0.1:8000/admin
    ## Próximos passos
    - Tela de cadastro para o cliente (fora do admin)
    - Login de usuários
    - Deploy online
      ## Autoria
      - Vitória Santos (https://www.linkedin.com/in/vitoria-santos-217332270/)
