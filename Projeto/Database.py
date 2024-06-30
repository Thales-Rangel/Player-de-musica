import sqlite3


class Banco:
    def __init__(self):
        conect = sqlite3.connect('database.db')

        cur = conect.cursor()

        cur.execute("""
            create table if not exists artistas(
                nome text primary key,
                foto blob
            )
        """)

        cur.execute("""
            create table if not exists albuns(
                nome text primary key,
                foto blob
            )
        """)

        cur.execute("""
            create table if not exists musicas(
                nome text primary key,
                minutos int,
                segundos int,
                album text,
                artista text,
                caminho text unique,
                foreign key (album) references albuns(nome),
                foreign key (artista) references artistas(nome)
            )
        """)

        cur.execute("""
            create table if not exists playlists(
                nome text primary key
            )
        """)

        cur.execute("""
            create table if not exists na_playlist(
                id integer primary key autoincrement,
                musica text,
                playlist text,
                foreign key (musica) references musicas(nome),
                foreign key (playlist) references playlists(nome)
            )
        """)

        try:
            cur.execute("insert into playlists values('Favoritas')")
        except sqlite3.IntegrityError:
            print("Playlist de favoritas já criada!")

        try:
            cur.execute("insert into artistas (nome) values ('Desconhecido')")
        except sqlite3.IntegrityError:
            print("Artista desconhecido já criado!")

        conect.commit()
        conect.close()

    @classmethod
    def conect(cls):
        Banco()
        conexao = sqlite3.connect('database.db')
        return conexao
