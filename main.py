import datetime

def ler_arquivo(arquivo):
    """
    Lê o arquivo fornecido pelo usuário e retorna os dados em uma lista de dicionários.
    """
    eventos = []
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                partes = linha.strip().split(',')
                if len(partes) != 6:
                    print(f"Linha ignorada (formato inválido): {linha}")
                    continue
                codigo, time, data_inicial, data_final, status, data_finalizacao = partes
                eventos.append({
                    'codigo': codigo.strip(),
                    'time': time.strip(),
                    'data_inicial': datetime.datetime.strptime(data_inicial.strip(), '%Y-%m-%d'),
                    'data_final': datetime.datetime.strptime(data_final.strip(), '%Y-%m-%d'),
                    'status': status.strip(),
                    'data_finalizacao': datetime.datetime.strptime(data_finalizacao.strip(), '%Y-%m-%d') if data_finalizacao.strip() else None
                })
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
    return eventos

def gerar_timeline(eventos):
    """
    Gera uma timeline em ASCII com base nos eventos fornecidos.
    """
    if not eventos:
        return "Nenhum evento para exibir."

    # Determinar o intervalo total da timeline
    data_min = min(evento['data_inicial'] for evento in eventos)
    data_max = max(evento['data_final'] for evento in eventos)
    for evento in eventos:
        if evento['data_finalizacao']:
            data_max = max(data_max, evento['data_finalizacao'])
    dias_totais = (data_max - data_min).days + 1

    # Criar a linha de datas
    linha_datas = []
    for i in range(dias_totais):
        data_atual_iterada = data_min + datetime.timedelta(days=i)
        linha_datas.append(data_atual_iterada.strftime('%d'))

    # Criar a linha de cabeçalho com os dias espaçados
    linha_datas_str = '|' + '|'.join(f"{dia:>2}" for dia in linha_datas) + '|'

    # Criar a linha do tempo
    timeline = []
    timeline.append(f"Timeline: {data_min.strftime('%Y-%m-%d')} até {data_max.strftime('%Y-%m-%d')}")
    timeline.append(" " * 20 + linha_datas_str)
    timeline.append(" " * 20 + "-" * len(linha_datas_str))

    for evento in eventos:
        codigo = evento['codigo']
        time = evento['time']
        data_inicial = evento['data_inicial']
        data_final = evento['data_final']
        status = evento['status']
        data_finalizacao = evento['data_finalizacao']

        # Calcular a posição inicial e final do evento na linha do tempo
        pos_inicial = (data_inicial - data_min).days
        pos_final = (data_final - data_min).days

        # Calcular a duração do evento em dias
        duracao = (data_final - data_inicial).days + 1

        # Criar a linha do evento
        linha_evento = ['  '] * dias_totais  # Dois espaços para cada dia
        for i in range(pos_inicial, pos_final + 1):
            linha_evento[i] = '##'  # Dois # para cada dia do evento

        # Verificar se há atraso
        atraso = 0
        if data_finalizacao and data_finalizacao > data_final:
            atraso = (data_finalizacao - data_final).days
            pos_finalizacao = (data_finalizacao - data_min).days
            for i in range(pos_final + 1, pos_finalizacao + 1):
                linha_evento[i] = '**'  # Dois * para cada dia de atraso

        # Juntar a linha com separadores
        linha_evento_str = '|' + '|'.join(linha_evento) + '|'

        # Adicionar a informação de atraso e datas, se houver
        atraso_str = f" ({atraso} dias atraso)" if atraso > 0 else ""
        datas_str = f"[{data_inicial.strftime('%d/%m')} - {data_final.strftime('%d/%m')}]"

        timeline.append(f"{codigo} ({time}): {linha_evento_str} ({duracao} dias){atraso_str} - {status} {datas_str}")

    return "\n".join(timeline)

def salvar_timeline(timeline, arquivo_saida):
    """
    Salva a timeline gerada em um arquivo de texto.
    """
    try:
        with open(arquivo_saida, 'w') as f:
            f.write(timeline)
        print(f"Timeline salva no arquivo: {arquivo_saida}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def main():
    print("Bem-vindo ao gerador de timeline em ASCII!")
    arquivo_entrada = input("Digite o nome do arquivo de entrada (ex: eventos.txt): ")
    arquivo_saida = input("Digite o nome do arquivo de saída (ex: timeline.txt): ")

    eventos = ler_arquivo(arquivo_entrada)
    if not eventos:
        print("Nenhum evento foi processado. Verifique o arquivo de entrada.")
        return

    timeline = gerar_timeline(eventos)
    print("\nTimeline gerada:\n")
    print(timeline)

    salvar_timeline(timeline, arquivo_saida)

if __name__ == "__main__":
    main()