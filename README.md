# 📅 Projeto Agenda | Django Contacts App
## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python)
![Django](https://img.shields.io/badge/Django-Yes-092E20?logo=django)
![SQLite](https://img.shields.io/badge/DB-SQLite-003B57?logo=sqlite)
![HTML](https://img.shields.io/badge/HTML-Templates-E34F26?logo=html5)
![CSS](https://img.shields.io/badge/CSS-Templates-1572B6?logo=css3)
![Virtualenv](https://img.shields.io/badge/Env-Virtualenv-4B8BBE?logo=python)

Aplicação web de agenda de contatos desenvolvida durante o curso [Python 3 do Zero ao Avançado](https://www.udemy.com/course/python-3-do-zero-ao-avancado) do Professor [Luiz Otávio](https://github.com/luizomf) com Python e Django, permitindo o gerenciamento completo de contatos (CRUD).

---

Projeto criado com foco em aprendizado, boas práticas e portfólio.

- Estrutura de projetos Django
- Models, Views e Templates
- Formulários
- Migrações e banco de dados
- Organização de arquivos estáticos e templates

## 🚀 Funcionalidades

- ✅ Listagem de contatos
- ✅ Cadastro de novos contatos
- ✅ Edição de contatos existentes
- ✅ Exclusão de contatos
- ✅ Interface web simples e intuitiva

## 📦 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- Python 3.8+
- pip
- virtualenv (ou venv)
- Git (opcional)

## ▶️ Como Executar o Projeto
### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/eriick-monteiro/projeto-agenda.git
cd projeto-agenda
```

### 2️⃣ Criar e ativar o ambiente virtual
```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar as migrações
```bash
python manage.py migrate
```

### 5️⃣ Iniciar o servidor
```bash
python manage.py runserver
```

Acesse no navegador:
```
http://127.0.0.1:8000
```

## 🧪 Testes

Caso queira rodar os testes:
```bash
python manage.py test
```

### 📁 Estrutura do Projeto
```bash
📦 projeto-agenda/
├── 📂 base_static/             # Arquivos estáticos (CSS, JS, imagens)
│   ├── 🎨 css/
│   ├── 🖼️ img/
│   └── 📜 js/
│
├── 📂 base_templates/          # Templates base
│   ├── 📂 global/
│   │   ├── 🧩 partials/
│   │   │   ├── 🔗 header.html
│   │   │   └── 🔗 footer.html
│   │   └── 🏗️ base.html
│
├── 📂 contact/                 # App de contatos
│   ├── 📂 migrations/
│   │   └── 🧱 __init__.py
│   ├── 📂 templates/
│   │   └── 📂 contact/
│   │       ├── 📄 index.html
│   │       ├── ➕ create.html
│   │       └── ✏️ update.html
│   ├── 📄 __init__.py
│   ├── 🧠 admin.py
│   ├── ⚙️ apps.py
│   ├── 📊 models.py
│   ├── 🧪 tests.py
│   ├── 🌐 urls.py
│   └── 👁️ views.py
│
├── 📂 project/                 # Configurações do Django
│   ├── 📄 __init__.py
│   ├── ⚙️ settings.py
│   ├── 🌐 urls.py
│   ├── 🔌 asgi.py
│   └── 🚀 wsgi.py
│
├── 📄 manage.py
├── 📄 requirements.txt
└── 📘 README.md
```

## 👤 Autor

Erick Monteiro  
GitHub: https://github.com/eriick-monteiro

## 📄 Licença

Este projeto é destinado a fins educacionais.
