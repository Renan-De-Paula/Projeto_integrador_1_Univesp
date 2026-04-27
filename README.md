# 🍰 Forno & Afeto - Sistema PDV (Executável)

Sistema de gestão (PDV) para confeitaria/padaria artesanal, desenvolvido com Django e distribuído em formato executável para uso simplificado.

---

## 📌 Sobre o Projeto

O **Forno & Afeto** é um sistema completo para gerenciamento de:

* Pedidos
* Clientes
* Produtos
* Financeiro

Esta versão foi empacotada para execução local sem necessidade de configuração manual avançada.

Projeto desenvolvido como parte do **Projeto Integrador da UNIVESP**.

---

## 🚀 Funcionalidades

* 📋 Cadastro de clientes
* 🧾 Controle de pedidos
* 🛒 Gestão de produtos
* 💰 Módulo financeiro
* 🔐 Acesso administrativo (Django Admin)
* 🌐 Interface web local (localhost)

---

## ▶️ Como Executar

### 🪟 Windows

1. Instale o **Python 3.10+**
   👉 https://www.python.org/downloads/
   ✔ Marque **"Add Python to PATH"**

2. Execute:

```
iniciar_Windows.bat
```

3. Acesse:

```
http://localhost:8000
```

---

### 🐧 Linux / 🍎 Mac

```bash
chmod +x iniciar_Mac_linux.sh
./iniciar.sh
```

Acesse:

```
http://localhost:8000
```

---

## 👤 Primeiro Acesso (Admin)

### Windows

```
criar_admin.bat
```

---

### Linux / Mac

```bash
source venv/bin/activate
cd sistema
python manage.py createsuperuser
```

Acesse:

```
http://localhost:8000/admin
```

---

## 🧩 Módulos do Sistema

| Módulo     | Rota           |
| ---------- | -------------- |
| Pedidos    | `/`            |
| Clientes   | `/clientes/`   |
| Produtos   | `/produtos/`   |
| Financeiro | `/financeiro/` |
| Admin      | `/admin/`      |

---

## 📂 Estrutura do Projeto

```
fornoAfeto/
│
├── iniciar.bat            # Inicialização no Windows
├── iniciar.sh             # Inicialização Linux/Mac
├── criar_admin.bat        # Criação de superusuário (Windows)
├── requirements.txt       # Dependências do projeto
│
└── sistema/               # Projeto Django
    │
    ├── manage.py
    │
    ├── core/              # Configurações principais (settings, urls)
    │
    ├── clientes/          # App de clientes
    ├── pedidos/           # App de pedidos
    ├── produtos/          # App de produtos
    ├── financeiro/        # App financeiro
    │
    ├── static/            # Arquivos estáticos (CSS, JS, imagens)
    └── templates/         # Templates HTML
```

---

## ⚠️ Problemas Comuns

### ❌ Python não encontrado

→ Reinstale marcando **Add to PATH**

---

### ❌ Porta 8000 em uso

→ Edite:

```
iniciar.bat
```

e altere para outra porta (ex: 8080)

---

### ❌ Erro no banco

→ Apague:

```
sistema/db.sqlite3
```

e execute novamente

---

## 👥 Integrantes

* [Renan de Paula](https://github.com/Renan-De-Paula)
* [Davi Higa](https://github.com/davihiga)
* [Lais Rocha](https://github.com/LaisRocha21)
* [Matheus Santos](https://github.com/Matt-ags)
* [Michelly Soares](https://github.com/mittyscarlet)
* [Raphaela Andrade](https://github.com/rapha4)
* [Suedson Silva](https://github.com/suedsonsilva-pixel)
* [Diego Silva](https://github.com/yofardiego)

---

## 📈 Status

✅ Sistema funcional
📦 Versão executável disponível
🚀 Pronto para uso local

---

## 📄 Licença

Projeto acadêmico - UNIVESP

---

## ⭐ Observações

* O sistema roda localmente via navegador
* Não necessita instalação manual completa (via scripts)
* Pode ser evoluído para ambiente de produção
* Contribuições são bem-vindas!

---

