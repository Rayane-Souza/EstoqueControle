# **Controle de Estoque - Projeto de Back-End (1ª Unidade)**

## **Descrição do Projeto**

Este é o projeto da primeira unidade da disciplina de back-end do 4º período, desenvolvido por Rayane Kelly, Ana Rodrigues, Rogério Rodrigues, Ana Silva e Luiz Sacramento. O objetivo do projeto é construir uma aplicação CRUD (Create, Read, Update, Delete) para o controle de estoque, utilizando o framework Django e o banco de dados SQLite para gerenciar e armazenar as informações.

A aplicação permite o gerenciamento completo dos itens de estoque, oferecendo uma interface simples para que o usuário possa adicionar, visualizar, editar e excluir produtos. Com essa solução, é possível monitorar de forma eficiente a quantidade de itens disponíveis e suas respectivas movimentações.

---

## **Tecnologias Utilizadas**

- **Django:** Framework web em Python que facilitou o desenvolvimento do back-end.
- **SQLite:** Banco de dados relacional leve e fácil de usar, integrado com o Django.
- **Python 3.10:** Linguagem de programação usada para o desenvolvimento da aplicação.
- **Tailwind CSS:** Framework CSS utilizado para estilizar as páginas de forma rápida e eficiente.
- **HTML/CSS:** Tecnologias básicas para a renderização de templates no front-end.

---

## **Capturas de Tela**

### **Tela Inicial - Listagem de Produtos**

![Listagem de Produtos](./my_project/static/img/Screenshot_1.png)

### **Tela de Cadastro de Produto**

![Cadastro de Produto](./my_project/static/img/Screenshot_2.png)

### **Tela de Edição de Produto**

![Edição de Produto](./my_project/static/img/Screenshot_3.png)

### **Tela de Deletar Produto**

![Edição de Produto](./my_project/static/img/Screenshot_4.png)

### **Tela de Visualizar Produto**
![image](https://github.com/user-attachments/assets/0b4b09a0-ac61-44be-a211-469bbdf9d38a)

### **Tela de Lista de Pagamentos**
![image](https://github.com/user-attachments/assets/47cda9ba-79da-46e8-8725-9b27b1baf136)

### **Tela de Novo Pagamento**
![image](https://github.com/user-attachments/assets/f2b8bf21-26e8-4c3d-9d69-dd6fa829dfe4)

### **Tela de Editar Pagamento**
![image](https://github.com/user-attachments/assets/7abf708e-84fd-4f63-be3c-6b7488ee9b77)

### **Tela de Deletar Pagamento**
![image](https://github.com/user-attachments/assets/064329cf-00b2-4f49-931b-c8e7114ebc1b)

### **Tela de Visualizar Pagamento**
![image](https://github.com/user-attachments/assets/c585507d-c2f9-4813-85fc-f7616b60bb56)

### **Tela de Lista de Pedidos**
![image](https://github.com/user-attachments/assets/059e2aee-bf2a-4a9b-994b-4f12860cd29f)

### **Tela de Novo Pedido**
![image](https://github.com/user-attachments/assets/dc5bd7e0-a4c7-4584-9049-b54db6739def)

### **Tela de Editar Pedido**
![image](https://github.com/user-attachments/assets/84eeb9de-f649-41b0-921f-138517fac897)

### **Tela de Deletar Pedido**
![image](https://github.com/user-attachments/assets/4d920462-2bcf-4f9e-9587-4db8a5089dd1)

### **Tela de Visualizar Pedido**
![image](https://github.com/user-attachments/assets/71c72944-eeef-40eb-93c0-448013845d48)



---
## **Estrutura do Diretório**

Aqui está uma visão geral da estrutura de pastas do projeto:


- **`manage.py`**: Script que facilita a execução de comandos administrativos, como migrações, execução do servidor, etc.
- **`db.sqlite3`**: Banco de dados SQLite utilizado para armazenar as informações do estoque.
- **`estoque`**: Diretório que contém o código principal da aplicação. Inclui as views (responsáveis pela lógica do CRUD), templates (HTML), models (definição das tabelas no banco), e urls (responsáveis pelo roteamento).

---

## **Funcionalidades**

## Produtos
1. **Cadastrar Produtos**: Permite adicionar novos itens ao estoque com informações como nome, quantidade e preço.
2. **Visualizar Produtos**: Exibe a lista de produtos no estoque.
3. **Editar Produtos**: Permite atualizar informações de um item do estoque.
4. **Deletar Produtos**: Remove itens do estoque quando não forem mais necessários.

## Pagamentos
1. **Cadastrar Pagamento**: Adiciona novo pagamento.
2. **Visualizar Pagamento**: Exibe o pagamento.
3. **Editar Pagamento**: Permite atualizar o pagamento.
4. **Deletar Pagamento**: Remove o pagamento.

## Pedidos
1. **Cadastrar Pedido**: Adiciona novo pedido.
2. **Visualizar Pedido**: Exibe o pedido.
3. **Editar Pedido**: Permite atualizar o pedido.
4. **Deletar Pedido**: Remove o pedido.

---

## **Como Executar o Projeto**

1. Clone o repositório:
   ```bash
   git clone https://github.com/Rayane-Souza/EstoqueControle.git
2. Entre no diretório do projeto:
   ```bash
   cd .\my_project\
3. Execute o servidor:
   ```bash
   python manage.py runserver
## Contribuidores

* Ana Silva
* Ana Rodrigues
* Luiz Sacramento
* Rayane Kelly
* Rogério Rodrigues



