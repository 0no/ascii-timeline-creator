# Gerador de Timeline ASCII 📅

Um programa Python que gera uma representação visual em ASCII de uma timeline de eventos, ideal para visualização de cronogramas de projetos e atividades.

## 📋 Características

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

1. python timeline_generator.py
1. **Siga as instruções**:

- Digite o nome do arquivo de entrada
- Digite o nome do arquivo de saída desejado

1. Timeline: 2023-11-25 até 2023-12-23                     |25|26|27|28|29|30|01|02|03|04|05|ATV-001 (Squad CRM): |##|##|##|##|##|##|##|##|##|##|  | (5 dias) - Concluído [25/11 - 05/12]

## 📊 Legenda da Timeline

- `|` : Separador de dias
- `##`: Dias de trabalho normal
- `**`: Dias em atraso
- ``  : Dias sem atividade

## 🎨 Exemplo de Saída

```
Timeline: 2023-11-25 até 2023-12-23                     |25|26|27|28|29|30|01|02|03|04|05|ATV-001 (Squad CRM): |##|##|##|##|##|##|##|##|##|##|  | (5 dias) - Concluído [25/11 - 05/12]ATV-002 (Squad CRM): |  |  |  |  |  |  |  |  |##|##|##| (3 dias) - Em andamento [09/12 - 11/12]
```

## ⚠️ Tratamento de Erros

O programa inclui tratamento para:

- Arquivo de entrada não encontrado
- Formato de data inválido
- Linhas mal formatadas no arquivo de entrada
- Erros de escrita no arquivo de saída

## 🤝 Contribuindo

Sinta-se à vontade para:

1. Reportar bugs
1. Sugerir novas funcionalidades
1. Enviar pull requests

## 📝 Notas

- As datas são exibidas no formato DD/MM para melhor legibilidade
- A duração é calculada automaticamente em dias
- O status "Atrasado" é atribuído automaticamente quando aplicável

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

