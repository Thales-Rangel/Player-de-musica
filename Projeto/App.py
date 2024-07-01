import mutagen.mp3

from GUIs import *
import os
from mutagen.mp3 import MP3
from Database import *
from Models import *

# O caminho será dado pelo usuário
caminho_das_musicas = ""

# Variavel que armazena o caminho absoluto do projeto
caminho_projeto = os.path.abspath('')

def centralizar_janela(janela):
    janela.update_idletasks()

    largura = janela.winfo_width()
    altura = janela.winfo_height()

    x = (janela.winfo_screenwidth() - largura) // 2
    y = (janela.winfo_screenheight() - altura) // 2 - 30

    janela.geometry(f"{largura}x{altura}+{x}+{y}")
    janela.deiconify()


def register_musics(caminho):
    con = Banco.conect()
    cur = con.cursor()

    # Esse comando altera o diretório de trabalho atual do programa para o expecificado no parametro
    os.chdir(caminho)
    #-------

    musics = os.listdir()

    for line in musics:
        name = os.path.splitext(line)[0]
        extension = os.path.splitext(line)[1]

        if extension == '.mp3':
            try:
                length = MP3(line).info.length

                sql_command = "insert into musicas values (?, ?, ?, ?, ?, ?)"
                try:
                    cur.execute("insert into albuns (nome) values (?)", (name,))
                except sqlite3.IntegrityError:
                    print(f'Album {name} já criado')

                try:
                    cur.execute(sql_command,
                                (name, length // 60, int(length % 60), name, "Desconhecido", os.path.abspath(line),))
                except sqlite3.IntegrityError:
                    print(f"Música {name} já criada")

            except mutagen.mp3.HeaderNotFoundError:
                print(f"Arquivo mp3 de {name} corrompido")

            con.commit()
    con.close()


register_musics(caminho_das_musicas)

# Após o comando register_musics alterar o diretório atual de trabalho para o caminho especificado das músicas
# Ele retorna ao diretório do projeto para os imports de imagens das classes em GUIs poderem funcionar
# Estava dando erro pois as classes em GUI estavam tentando buscar imagens em um diretório diferente da pasta Img
os.chdir(os.path.abspath(caminho_projeto))

app = App()

centralizar_janela(app)

app.mainloop()
