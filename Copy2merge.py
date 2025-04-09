import os
import shutil
from datetime import datetime

def solicitar_entrada():
    origem = input("Digite o caminho da pasta de origem: ").strip()
    destino = input("Digite o caminho da pasta de destino: ").strip()
    
    # Informe o padrão das datas para o usuário, no exemplo "dd/mm/aaaa"
    data_inicial_str = input("Digite a data inicial (dd/mm/aaaa): ").strip()
    data_final_str = input("Digite a data final (dd/mm/aaaa): ").strip()
    
    # Converter as datas para objetos datetime
    data_inicial = datetime.strptime(data_inicial_str, '%d/%m/%Y')
    data_final = datetime.strptime(data_final_str, '%d/%m/%Y')
    return origem, destino, data_inicial, data_final

def copiar_arquivos(origem, destino, data_inicial, data_final):
    # Define as extensões permitidas (em minúsculas)
    extensoes_permitidas = {'.pa', '.pa3', '.tr', '.tr3'}

    # Caso a pasta de destino não exista, cria-a
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Contador de arquivos copiados
    contagem = 0

    # Percorre recursivamente as pastas da origem
    for root, dirs, files in os.walk(origem):
        for arquivo in files:
            # Verifica se o arquivo possui alguma das extensões permitidas
            if any(arquivo.lower().endswith(ext) for ext in extensoes_permitidas):
                caminho_completo = os.path.join(root, arquivo)
                # Obtém a data de modificação do arquivo
                mod_time = datetime.fromtimestamp(os.path.getmtime(caminho_completo))
                # Verifica se a data de modificação está entre a data inicial e final (inclusive)
                if data_inicial <= mod_time <= data_final:
                    # Copia o arquivo para a pasta de destino
                    # Se desejar manter a estrutura original das pastas, pode reconstruir o caminho relativo.
                    shutil.copy2(caminho_completo, destino)
                    print(f"Arquivo {caminho_completo} copiado.")
                    contagem += 1

    print(f"\nTotal de arquivos copiados: {contagem}")

if __name__ == "__main__":
    origem, destino, data_inicial, data_final = solicitar_entrada()
    copiar_arquivos(origem, destino, data_inicial, data_final)
