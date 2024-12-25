#!/bin/bash

# Verificar se o Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "Docker não está instalado. Por favor, instale o Docker primeiro."
    exit 1
fi

# Verificar se o docker-compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose não está instalado. Por favor, instale o Docker Compose primeiro."
    exit 1
fi

# Limpar builds anteriores
echo "Limpando builds anteriores..."
rm -rf build dist *.spec

# Construir a imagem Docker
echo "Construindo imagem Docker..."
docker-compose build

# Executar o container para criar o executável
echo "Criando executável..."
docker-compose run builder

# Verificar se o executável foi criado
if [ -f "dist/TimelineGenerator" ]; then
    echo "Executável criado com sucesso em dist/TimelineGenerator"
else
    echo "Erro ao criar o executável"
    exit 1
fi