executar os seguintes comandos após desinstalar a pasta .venv: 
python -m venv .venv
● Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
./.venv/Scripts/activate
pip install django
pip install black
black .