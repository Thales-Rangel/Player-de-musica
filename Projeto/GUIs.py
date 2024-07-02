from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL.ImageTk import PhotoImage

from Models import *

fonte_padrao = ("verdana", 12)

# Carregando as imagens
img_home = Image.open('Img/Home_Icon.png')
img_favorite = Image.open('Img/Favorite_Icon.png')
img_artist = Image.open('Img/Artist_Icon.png')
img_albums = Image.open('Img/Albun_Icon.png')
img_playlists = Image.open('Img/Playlists_Icon.png')
img_play = Image.open('Img/music_play_icon.png')
img_loved_track = Image.open('Img/Loved_track_Icon.png')
img_search = Image.open('Img/search_icon.png')


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Player de Música")
        self.geometry("1200x720")

        nav = Frame(self, width=90, borderwidth=1, relief="solid")
        nav.pack(side="left", fill='both')

        #Carregado os icones para os botoes da NavBar
        img_home_icon: PhotoImage = ImageTk.PhotoImage(img_home.resize((40, 40)))
        img_favorite_icon: PhotoImage = ImageTk.PhotoImage(img_favorite.resize((40, 40)))
        img_artist_icon: PhotoImage = ImageTk.PhotoImage(img_artist.resize((40, 40)))
        img_albums_icon: PhotoImage = ImageTk.PhotoImage(img_albums.resize((40, 40)))
        img_playlists_icon: PhotoImage = ImageTk.PhotoImage(img_playlists.resize((40, 40)))

        botao_home = Button(nav, image=img_home_icon, bd=0, command=lambda: self.show_frame(StartPage))
        botao_home.imagem = img_home_icon
        botao_home.place(x=20, y=5)

        botao_favorite = Button(nav, image=img_favorite_icon, bd=0, command=lambda: self.show_frame(Page1))
        botao_favorite.imagem = img_favorite_icon
        botao_favorite.place(x=20, y=55)

        botao_artists = Button(nav, image=img_artist_icon, bd=0, command=lambda: self.show_frame(Page1))
        botao_artists.imagem = img_artist_icon
        botao_artists.place(x=20, y=105)

        botao_albums = Button(nav, image=img_albums_icon, bd=0, command=lambda: self.show_frame(Page1))
        botao_albums.imagem = img_albums_icon
        botao_albums.place(x=20, y=155)

        botao_playlists = Button(nav, image=img_playlists_icon, bd=0, command=lambda: self.show_frame(Page1))
        botao_playlists.imagem = img_playlists_icon
        botao_playlists.place(x=20, y=205)

        self.container = Frame(self)
        self.container.pack(side="left", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Page1):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

        self.player = Player(self)

    def show_frame(self, count):
        frame = self.frames[count]
        frame.tkraise()

    def show_player(self):
        self.player.pack(side="right", fill="both")


class Player(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, width=325, borderwidth=1, relief="solid")

        #Carregar as imagens
        exit_icon: PhotoImage = ImageTk.PhotoImage(Image.open('Img/Exit_icon.png').resize((20, 20)))
        more_options_icon: PhotoImage = ImageTk.PhotoImage(Image.open('Img/more-options-icon.png').resize((40, 40)))
        fila_de_reproducao_icon: PhotoImage = ImageTk.PhotoImage(img_playlists.resize((30, 30)))

        img_play_icon: PhotoImage = ImageTk.PhotoImage(img_play.resize((55, 55)))
        img_pause_icon: PhotoImage = ImageTk.PhotoImage(Image.open('Img/music_pause_icon.png').resize((55, 55)))
        img_previous_icon: PhotoImage = ImageTk.PhotoImage(
            Image.open('Img/music_previous_icon.png').resize((40, 40)))
        img_next_icon: PhotoImage = ImageTk.PhotoImage(
            Image.open('Img/music_next_player_track_icon.png').resize((40, 40)))
        img_aleat_icon: PhotoImage = ImageTk.PhotoImage(
            Image.open('Img/music_player_shuffle_song_icon.png').resize((25, 25)))
        img_repeat_icon: PhotoImage = ImageTk.PhotoImage(
            Image.open('Img/music_refresh_repeat_song_icon.png').resize((40, 40)))
        img_once_repeat_icon: PhotoImage = ImageTk.PhotoImage(
            Image.open('Img/music_once_refresh_repeat_icon.png').resize((40, 40)))
        self.img_loved_track_icon: PhotoImage = ImageTk.PhotoImage(img_loved_track.resize((30, 30)))
        self.img_no_loved_track_icon: PhotoImage = ImageTk.PhotoImage(img_favorite.resize((25, 25)))

        sair = Button(self, image=exit_icon, bd=0, command=lambda: parent.player.pack_forget())
        sair.imagem = exit_icon
        sair.place(x=270, y=15)

        self.imagem: PhotoImage = ImageTk.PhotoImage(Image.open('Img/Icone_Music.png').resize((265, 265)))

        self.icone = Label(self, image=self.imagem, borderwidth=1, relief="solid")
        self.icone.place(x=30, y=60)

        more_options = Button(self, image=more_options_icon, bd=0)
        more_options.imagem = more_options_icon
        more_options.place(x=142, y=360)

        self.fila_de_reproducao = Button(self, image=fila_de_reproducao_icon, bd=0)
        self.fila_de_reproducao.imagem = fila_de_reproducao_icon
        self.fila_de_reproducao.place(x=217, y=365)

        self.barra_de_reproducao = ttk.Scale(self, from_=0, to=100, orient=HORIZONTAL, value=0, length=300)
        self.barra_de_reproducao.place(x=10, y=430)

        self.nome_musica = Label(self, text="Nome da música", font=fonte_padrao)
        self.nome_musica.place(x=10, y=480)

        self.play_button = Button(self, image=img_play_icon, bd=0)
        self.play_button.imagem = img_play_icon
        self.play_button.place(x=135, y=530)

        self.next_button = Button(self, image=img_next_icon, bd=0)
        self.next_button.imagem = img_next_icon
        self.next_button.place(x=210, y=537)

        self.previous_button = Button(self, image=img_previous_icon, bd=0)
        self.previous_button.imagem = img_previous_icon
        self.previous_button.place(x=75, y=537)

        self.order_button = Button(self, image=img_aleat_icon, bd=0)
        self.order_button.imagem = img_aleat_icon
        self.order_button.place(x=25, y=544)

        self.loved_button = Button(self, image=self.img_no_loved_track_icon, bd=0, command=self.loved)
        self.loved_button.imagem = self.img_no_loved_track_icon
        self.loved_button.place(x=275, y=544)

    def loved(self):
        if self.loved_button.imagem == self.img_loved_track_icon:
            self.loved_button.configure(image=self.img_no_loved_track_icon)
            self.loved_button.imagem = self.img_no_loved_track_icon
            self.loved_button.place(x=275, y=544)
        else:
            self.loved_button.configure(image=self.img_loved_track_icon)
            self.loved_button.imagem = self.img_loved_track_icon
            self.loved_button.place(x=271, y=542)


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        search_area = Frame(self, borderwidth=1, relief="solid", padx=10, pady=30)
        search_area.pack(side="top", fill="both")

        self.search = Entry(search_area, font=fonte_padrao, width=30)
        self.search.bind("<Return>", self.pesquisa)
        self.search.pack(side="left")

        self.search_icon: PhotoImage = ImageTk.PhotoImage(img_search.resize((20, 20)))
        Label(search_area, image=self.search_icon).pack(side="left")

        self.botao = Button(self, text="Player", command=lambda: controller.show_player())
        self.botao.pack()

        container = Frame(self)
        container.grid_columnconfigure(0, weight=1)
        container.pack(side="left", fill="both", expand=True)

        canvas = Canvas(container)

        s = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)

        self.list_cards = Frame(canvas, borderwidth=2, relief='solid')
        self.list_cards.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.list_cards.pack(fill="both", expand=True)
        canvas.create_window((0, 0), window=self.list_cards, anchor="nw")

        canvas.configure(yscrollcommand=s.set)

        canvas.pack(side="left", fill="both", expand=True)
        s.pack(side="right", fill="y")

        for i in range(5):
            self.list_cards.grid_columnconfigure(i, weight=1)

        self.cards = []
        self.create_cards()

        coluna = 0
        linha = 0
        for card in self.cards:
            card.grid(sticky='nsew', column=coluna, row=linha, pady=5, padx=5)
            if coluna < 4:
                coluna = coluna+1
            else:
                coluna = 0
                linha = linha+1

    def create_cards(self):
        con = Banco.conect()
        cur = con.cursor()

        res = cur.execute("select * from musicas")

        for line in res:
            self.cards.append((Card(self.list_cards, Music(line[0], con))))
        con.close()

    def pesquisa(self, event):
        print(f"Pesquisa: {self.search.get()}")
        self.search.delete(0, END)


class Card(Frame):
    def __init__(self, parent, musica):
        Frame.__init__(self, parent, borderwidth=2, relief='solid')

        capa: PhotoImage = ImageTk.PhotoImage(musica.album.foto.resize((133, 133)))
        icon_play = ImageTk.PhotoImage(img_play.resize((30, 30)))

        capa_album = Label(self, image=capa)
        capa_album.imagem = capa
        capa_album.pack(side="top")

        play = Button(self, image=icon_play)
        play.imagem = icon_play
        play.pack(side="bottom")


class Page1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, background='red')
