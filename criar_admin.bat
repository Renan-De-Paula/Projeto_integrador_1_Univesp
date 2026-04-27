@echo off
title Forno e Afeto - Criar Admin
echo.
echo  Criando usuario administrador...
echo.

if not exist "venv\" (
    echo  [ERRO] Execute primeiro o iniciar.bat!
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
cd sistema
python manage.py createsuperuser

echo.
echo  Usuario criado! Acesse http://localhost:8000/admin
pause
