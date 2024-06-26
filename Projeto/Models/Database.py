import sqlite3
from PIL import Image


class Banco:
    def __init__(self):
        conect = sqlite3.connect('database.db')

        self.cur = conect.cursor()

        self.cur.execute("""
            create table if not exists artistas(
                nome text primary key,
                foto blob
            )
        """)

        self.cur.execute("""
            create table if not exists albuns(
                nome text primary key,
                foto blob
            )
        """)

        self.cur.execute("""
            create table if not exists musicas(
                nome text primary key,
                minutos int,
                segundos int,
                album text,
                artista text,
                caminho text,
                foreign key (album) references albuns(nome),
                foreign key (artista) references artistas(nome)
            )
        """)

        self.cur.execute("""
            create table if not exists playlists(
                nome text primary key
            )
        """)

        self.cur.execute("""
            create table if not exists na_playlist(
                id integer primary key autoincrement,
                musica text,
                playlist text,
                foreign key (musica) references musicas(nome),
                foreign key (playlist) references playlists(nome)
            )
        """)

        try:
            self.cur.execute("insert into playlists values('Favoritas')")
            conect.commit()
        except sqlite3.IntegrityError:
            print("Playlist de favoritas já criada!")

        conect.close()

    @classmethod
    def conect(cls):
        Banco()
        conexao = sqlite3.connect('database.db')
        return conexao
