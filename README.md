# ASCII Timeline Generator 📅

A Python program that generates an ASCII visual representation of event timelines, perfect for visualizing project schedules and activities.

## 🌟 Available in Two Languages

- [English](#english)
- [Português](#português)

# English

## 📋 Features

- CSV file event reading
- ASCII visualization with vertical separators
- Support for different event statuses (Completed, In Progress, Not Started)
- Delay indication with special markers
- Start and end date display
- Automatic event duration calculation
- Timeline export to text file

## 🔧 Requirements

- Python 3.6 or higher
- Standard library modules:
  - datetime
  - csv (optional, for CSV file reading)

## 📁 Input File Format

The input file should be a CSV file with the following columns:

```
Code,Team,Start Date,End Date,Status,Completion DateATV-001,CRM Squad,2023-11-25,2023-12-05,Completed,2023-12-05
```

### Required Columns:

- **Code**: Unique activity identifier (e.g., ATV-001)
- **Team**: Responsible team name
- **Start Date**: Start date in YYYY-MM-DD format
- **End Date**: Expected end date in YYYY-MM-DD format
- **Status**: Current status (Completed, In Progress, Not Started)
- **Completion Date**: Actual completion date (optional)

## 🚀 How to Use

1. Run the program:

```
python timeline_generator.py
```

1. Follow the prompts:

- Enter input file name
- Enter desired output file name

## 📊 Timeline Legend

- `|` : Day separator
- `##`: Normal working days
- `**`: Delayed days
- ``  : Days without activity

## 🎨 Output Example

```
Timeline: 2023-11-25 to 2023-12-23                     |25|26|27|28|29|30|01|02|03|04|05|ATV-001 (CRM Squad): |##|##|##|##|##|##|##|##|##|##|  | (5 days) - Completed [25/11 - 05/12]
```

## ⚠️ Error Handling

The program includes handling for:

- Input file not found
- Invalid date format
- Malformed lines in input file
- Output file writing errors

---

# Português

## 📋 Funcionalidades

- Leitura de eventos a partir de arquivo CSV
- Visualização em ASCII com separadores verticais
- Suporte a diferentes status de eventos (Concluído, Em andamento, Não iniciado)
- Indicação de atrasos com marcadores especiais
- Exibição de datas de início e fim
- Cálculo automático de duração dos eventos
- Exportação da timeline para arquivo texto

## 🔧 Requisitos

- Python 3.6 ou superior
- Módulos da biblioteca padrão:
  - datetime
  - csv (opcional, para leitura de arquivos CSV)

## 📁 Formato do Arquivo de Entrada

O arquivo de entrada deve ser um arquivo CSV com as seguintes colunas:

```
Código,Time,Data Inicial,Data Final,Status,Data FinalizaçãoATV-001,Squad CRM,2023-11-25,2023-12-05,Concluído,2023-12-05
```

### Colunas Obrigatórias:

- **Código**: Identificador único da atividade (ex: ATV-001)
- **Time**: Nome da equipe responsável
- **Data Inicial**: Data de início no formato YYYY-MM-DD
- **Data Final**: Data prevista de término no formato YYYY-MM-DD
- **Status**: Status atual (Concluído, Em andamento, Não iniciado)
- **Data Finalização**: Data real de conclusão (opcional)

## 🚀 Como Usar

1. Execute o programa:

```
python timeline_generator.py
```

1. Siga as instruções:

- Digite o nome do arquivo de entrada
- Digite o nome do arquivo de saída desejado

## 📊 Legenda da Timeline

- `|` : Separador de dias
- `##`: Dias de trabalho normal
- `**`: Dias em atraso
- ``  : Dias sem atividade

## 🎨 Exemplo de Saída

```
Timeline: 2023-11-25 até 2023-12-23                     |25|26|27|28|29|30|01|02|03|04|05|ATV-001 (Squad CRM): |##|##|##|##|##|##|##|##|##|##|  | (5 dias) - Concluído [25/11 - 05/12]
```

## ⚠️ Tratamento de Erros

O programa inclui tratamento para:

- Arquivo de entrada não encontrado
- Formato de data inválido
- Linhas mal formatadas no arquivo de entrada
- Erros de escrita no arquivo de saída

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.