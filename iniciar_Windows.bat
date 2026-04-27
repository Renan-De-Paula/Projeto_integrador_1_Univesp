@echo off
title Forno e Afeto - PDV

echo.
echo  ============================================
echo      FORNO E AFETO - Sistema PDV
echo  ============================================
echo.

:: Verifica Python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo  [ERRO] Python nao encontrado!
    echo  Instale em: https://www.python.org/downloads/
    echo  Marque a opcao Add Python to PATH!
    pause
    exit /b 1
)
echo  [OK] Python encontrado.

:: Cria ambiente virtual se nao existir
if not exist "venv\" (
    echo  [INSTALANDO] Criando ambiente virtual...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo  [ERRO] Falha ao criar ambiente virtual!
        pause
        exit /b 1
    )
)

:: Ativa ambiente virtual
call venv\Scripts\activate.bat

:: Instala dependencias
echo  [INSTALANDO] Verificando dependencias...
pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo  [ERRO] Falha ao instalar dependencias!
    pause
    exit /b 1
)

:: Entra na pasta do projeto
cd sistema

:: Executa migracoes
echo  [BANCO] Configurando banco de dados...
python manage.py migrate --run-syncdb >nul 2>&1

:: Coleta arquivos estaticos
echo  [STATIC] Coletando arquivos estaticos...
python manage.py collectstatic --noinput >nul 2>&1

echo.
echo  ============================================
echo   Sistema iniciado com sucesso!
echo   Acesse: http://localhost:8000
echo.
echo   Pressione Ctrl+C para encerrar.
echo  ============================================
echo.

:: Abre navegador
start "" "http://localhost:8000"

:: Inicia servidor com waitress
python -c "from waitress import serve; from core.wsgi import application; import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings'); serve(application, host='0.0.0.0', port=8000)"

pause
