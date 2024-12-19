## Sobre
O <b>GoFood</b> é uma API RESTful desenvolvida para simplificar e otimizar a gestão de entregas e pedidos. Os clientes podem realizar pedidos de forma prática, aplicar cupons de desconto, escolher entre diversas formas de pagamento e acompanhar o status da entrega. Com recursos como cálculo automático de valores, gerenciamento de endereços e opções personalizadas para cada pedido. Além disso, o sistema oferece um dashboard de gerenciamento para administradores, permitindo gerenciar pedidos, acompanhar o desempenho do delivery, cadastrar produtos, criar cupons promocionais e visualizar relatórios detalhados.

### Desenvolvido com as seguintes tecnologias:
- Python
- Django
- DRF (Django Rest Framework)
- PostgreSQL
- Docker
- Swagger para **Documentação**

### Documentação Swagger
![Captura de tela_19-12-2024_12817_localhost](https://github.com/user-attachments/assets/dbed51fa-3902-4ff7-b807-aabf780c5591)

### Modelagem
![Captura de tela 2024-12-19 120549](https://github.com/user-attachments/assets/85e5a9dc-0d3c-408d-aebd-484539a4b94c)

### Passo a passo para inicialização

<h5>Ambiente virtual</h5>

1. Faça o Download do zip do projeto ou clone o repositório Git e extraia o conteúdo do arquivado compactado
2. Navegue até a pasta do projeto e abra o Prompt de Comando do Windows ou Terminal do GNU/Linux
4. Execute o comando `sudo apt install python3.12-venv`. Instala o pacote python3.12-venv que fornece ferramentas para criar ambientes virtuais
5. Execute o comando `python3 -m venv venv`. Cria um novo ambiente virtual chamado 'venv' usando o Python 3
6. Execute o comando `source venv/bin/activate`. Ativa o ambiente virtual 
7. Execute o comando `pip install -r requirements.txt`. Instala as dependências listadas no arquivo requirements.txt
8. Execute o comando `python manage.py makemigrations`. Cria novos arquivos de migração com base nas alterações feitas nos modelos
9. Execute o comando `python manage.py migrate`. Aplica as migrações pendentes ao banco de dados
10. Execute o comando `python manage.py createsuperuser`. Inicia o processo de criação do superu-suário

<h5>Ambiente docker</h5>

1. Baixe e instale o Docker Desktop
2. Execute o comando `docker-compose build`. Contruir novas imagens a parti do Dockfile
3. Execute o comando `docker-compose up -d`. Inicializar os contêineres da aplicação
4. Execute o comando `docker-compose exec gofood-app-1 bash`. Abra um shell no contêiner
5. Execute o comando `python manage.py makemigrations`. Cria novos arquivos de migração com base nas alterações feitas nos modelos (dentro do contêiner)
6. Execute o comando `python manage.py migrate`. Aplica as migrações pendentes ao banco de dados (dentro do contêiner)
7. Execute o comando `python manage.py createsuperuser`. Inicia o processo de criação do superu-suário (dentro do contêiner)

Acessar a aplicação
[http://localhost:8000](http://localhost:8000)
