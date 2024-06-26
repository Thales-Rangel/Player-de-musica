import PIL
import io
from PIL import Image

from Database import Banco


def convert_to_binary(caminho):
    with open(caminho, 'rb') as file:
        blob_data = file.read()
    return blob_data


class Music:
    def __init__(self, name, con):
        cur = con.cursor()

        res = cur.execute(f"select * from musicas where nome = '{name}'")

        for line in res:
            self.nome = name
            self.tempo = (line[1], line[2])
            self.album = Album(line[3], con)
            self.artista = Artist(line[4], con)
            self.caminho = line[5]


class Album:
    def __init__(self, name, con):
        cur = con.cursor()

        res = cur.execute(f"select * from albuns where nome = '{name}'")

        for line in res:
            self.nome = name
            try:
                self.foto = Image.open(io.BytesIO(line[1]))
            except PIL.UnidentifiedImageError:
                self.foto = Image.open('Img/Icone_Music.png')
                cur.execute("update albuns set foto = ? where nome = ?",
                            (convert_to_binary('Img/Icone_Music.png'), name,))
                con.commit()


class Artist:
    def __init__(self, name, con):
        cur = con.cursor()

        res = cur.execute(f"select * from artistas where nome = '{name}'")

        for line in res:
            self.nome = name
            try:
                self.foto = Image.open(io.BytesIO(line[1]))
            except PIL.UnidentifiedImageError:
                self.foto = Image.open('Img/Default_Image_Artist.jpg')
                cur.execute("update artistas set foto = ? where nome = ?",
                            (convert_to_binary('Img/Default_Image_Artist.jpg'), name,))
                con.commit()



class Playlist:
    def __init__(self, name):
        con = Banco.conect()
        cur = con.cursor()

        res = cur.execute(f"select * from playlists where nome = '{name}'")

        for line in res:
            self.nome = line[0]

        self.musicas = []
        res = cur.execute(f"select musica from na_playlist where playlist = '{name}'")
        for line in res:
            self.musicas.append(Music(line[0]))

        con.close()
