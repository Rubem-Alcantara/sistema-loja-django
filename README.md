# Sistema de Gestão de Loja (Django Full)

Projeto desenvolvido para a 2ª EA da disciplina de Programação Backend. O sistema evoluiu de um formulário simples para um ERP completo com Dashboard, Controle de Estoque e Segurança.

## 🎯 Objetivos do Projeto
O objetivo inicial era compreender o funcionamento do Framework Django através da criação de formulários (`ModelForm`) e inserção de dados. O projeto foi expandido para simular um ambiente real de produção.

## 🚀 Funcionalidades Implementadas

### Requisitos Obrigatórios (Cumpridos):
* ✅ **Modelagem:** Criação da classe `Produto`.
* ✅ **Templates:** Uso de herança (`base.html` e `block content`).
* ✅ **Forms:** Implementação de `forms.ModelForm`.
* ✅ **Views:** Lógica de cadastro via requisição POST.

### Funcionalidades Extras (Diferenciais):
* 📊 **Dashboard Administrativo:** Painel exclusivo para gerentes com KPIs (Total de Vendas, Valor em Estoque) e tabela de alerta para **Estoque Baixo**.
* 📸 **Gestão de Mídia:** Upload de imagens dos produtos usando biblioteca `Pillow`.
* 🏷️ **Categorização:** Relacionamento 1:N entre Produtos e Categorias.
* 🔐 **Segurança Avançada:**
    * Sistema de Login/Logout e Cadastro de Usuários.
    * Proteção de rotas com `@login_required` e `@user_passes_test`.
    * Diferenciação de permissões (Vendedor vs. Gerente).
    * Proteção de Variáveis de Ambiente com `.env`.
* 🎨 **Interface:** Design responsivo utilizando **Bootstrap 5** e ícones Bootstrap Icons.
* 🔍 **Ferramentas de Busca:** Filtro de produtos por nome.

## 🛠️ Tecnologias Utilizadas
* Python 3.12
* Django 5.2
* Bootstrap 5
* SQLite
* Python-Dotenv

## 🔧 Como rodar o projeto localmente
1. Clone o repositório.
2. Crie o ambiente virtual: `python -m venv venv`
3. Instale as dependências: `pip install -r requirements.txt`
4. Crie o arquivo `.env` na raiz e adicione sua `SECRET_KEY` e `DEBUG=True`.
5. Execute as migrações: `python manage.py migrate`
6. Crie um superusuário: `python manage.py createsuperuser`
7. Inicie o servidor: `python manage.py runserver`
