#!/bin/bash

echo ""
echo " ============================================"
echo "     FORNO E AFETO - Sistema PDV"
echo " ============================================"
echo ""

# Verifica se Python esta instalado
if ! command -v python3 &> /dev/null; then
    echo " [ERRO] Python3 nao encontrado!"
    echo ""
    echo " Instale com:"
    echo "   Ubuntu/Debian: sudo apt install python3 python3-pip python3-venv"
    echo "   Mac: brew install python3"
    echo ""
    exit 1
fi

echo " [OK] Python encontrado: $(python3 --version)"

# Diretorio do script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Cria ambiente virtual se nao existir
if [ ! -d "venv" ]; then
    echo ""
    echo " [INSTALANDO] Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativa ambiente virtual
source venv/bin/activate

# Instala dependencias
echo " [INSTALANDO] Verificando dependencias..."
pip install -r requirements.txt --quiet

# Entra na pasta do projeto
cd sistema

# Executa migracoes
echo " [BANCO] Configurando banco de dados..."
python manage.py migrate --run-syncdb > /dev/null 2>&1

# Coleta arquivos estáticos
echo " [STATIC] Coletando arquivos estaticos..."
python manage.py collectstatic --noinput > /dev/null 2>&1

echo ""
echo " ============================================"
echo "  Sistema iniciado com sucesso!"
echo "  Acesse: http://localhost:8000"
echo ""
echo "  Pressione Ctrl+C para encerrar."
echo " ============================================"
echo ""

# Abre navegador (tenta diferentes comandos)
(sleep 2 && (xdg-open "http://localhost:8000" || open "http://localhost:8000") 2>/dev/null) &

# Inicia com waitress
python -c "
from waitress import serve
from core.wsgi import application
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
print('Servidor rodando em http://localhost:8000')
serve(application, host='0.0.0.0', port=8000)
"
