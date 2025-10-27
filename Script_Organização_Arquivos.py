import os
import shutil

caminho_pasta_downloads = os.path.expanduser('~\Downloads')

lista_conteudo_downloads = os.listdir(caminho_pasta_downloads)

extensoes_documentos = ['.pdf', '.PDF', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx']
extensoes_imagens = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
extensoes_videos = ['.mp4', '.avi', '.mov', '.mkv', '.flv']
extensoes_musicas = ['.mp3', '.wav', '.aac', '.flac']
extensoes_comprimidos = ['.zip', '.rar', '.7z', '.tar', '.gz']
extensoes_programas = ['.exe', '.msi', '.dmg', '.pkg', '.py', '.ics', '.epub']

# 🔧 Dicionário que agrupa as extensões por categoria
# Isso permite iterar de forma mais organizada e evitar repetição de código
categorias = {
    "documentos": extensoes_documentos,
    "imagens": extensoes_imagens,
    "videos": extensoes_videos,
    "musicas": extensoes_musicas,
    "comprimidos": extensoes_comprimidos,
    "programas": extensoes_programas
}

# 📂 Loop principal que percorre todos os arquivos na pasta de downloads
for conteudo in lista_conteudo_downloads:
    
    # 🔍 Para cada categoria, verifica se o arquivo pertence a ela
    for categoria, extensoes in categorias.items():
        for extensao in extensoes:
            if extensao in conteudo:
                
                # 🖨️ Exibe no terminal o tipo de arquivo identificado
                print(f'Arquivo ({conteudo}) é uma {extensao}.')
                
                # 📌 Define os caminhos de origem e destino do arquivo
                caminho_origem = os.path.join(caminho_pasta_downloads, conteudo)
                nova_pasta = os.path.join(caminho_pasta_downloads, categoria)
                caminho_destino = os.path.join(nova_pasta, conteudo)

                # 📁 Cria a pasta de destino se ela ainda não existir
                if not os.path.exists(nova_pasta):
                    os.makedirs(nova_pasta)

                # 🚚 Tenta mover o arquivo para a nova pasta
                try:
                    shutil.move(caminho_origem, caminho_destino)
                except FileNotFoundError:
                    print(f"Erro: O arquivo de origem ou a pasta de destino não foi encontrado.")
                except Exception as e:
                    print(f"Ocorreu um erro ao mover o arquivo: {e}")
                
                # ✅ Interrompe o loop após encontrar a primeira categoria correspondente
                break