import PyInstaller.__main__
import os

# Configurações do executável
PyInstaller.__main__.run([
    'main.py',  # seu arquivo principal
    '--onefile',             # criar um único arquivo executável
    '--console',             # manter o console (já que é uma aplicação de linha de comando)
    '--name=TimelineGenerator',  # nome do executável
    '--clean',               # limpar cache antes de construir
    '--add-data=README.md:.' # (opcional) incluir o README
])

# '--icon=icon.ico',