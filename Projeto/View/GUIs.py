from tkinter import *
from PIL import Image, ImageTk

# Carregando as imagens
img_home = Image.open('../Img/Home_Icon.png')
img_favorite = Image.open('../Img/Favorite_Icon.png')
img_artist = Image.open('../Img/Artist_Icon.png')
img_albums = Image.open('../Img/Albun_Icon.png')
img_playlists = Image.open('../Img/Playlists_Icon.png')

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        nav = Frame(self, width=90, borderwidth=1, relief="solid")
        nav.pack(side="left", fill='both')

        #Carregado os icones para os botões da NavBar
        img_home_icon = ImageTk.PhotoImage(img_home.resize((40, 40)))
        img_favorite_icon = ImageTk.PhotoImage(img_favorite.resize((40, 40)))
        img_artist_icon = ImageTk.PhotoImage(img_artist.resize((40, 40)))
        img_albums_icon = ImageTk.PhotoImage(img_albums.resize((40, 40)))
        img_playlists_icon = ImageTk.PhotoImage(img_playlists.resize((40, 40)))

        botao_home = Button(nav, image=img_home_icon,command=lambda: self.show_frame(StartPage))
        botao_home.imagem = img_home_icon
        botao_home.place(x=20, y=5)

        botao_favorite = Button(nav, image=img_favorite_icon, command=lambda: self.show_frame(Page1))
        botao_favorite.imagem = img_favorite_icon
        botao_favorite.place(x=20, y=55)

        botao_artists = Button(nav, image=img_artist_icon, command=lambda: self.show_frame(Page1))
        botao_artists.imagem = img_artist_icon
        botao_artists.place(x=20, y=105)

        botao_albums = Button(nav, image=img_albums_icon, command=lambda: self.show_frame(Page1))
        botao_albums.imagem = img_albums_icon
        botao_albums.place(x=20, y=155)

        botao_playlists = Button(nav, image=img_playlists_icon, command=lambda: self.show_frame(Page1))
        botao_playlists.imagem = img_playlists_icon
        botao_playlists.place(x=20, y=205)

        container = Frame(self)
        container.pack(side="left", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Page1):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, count):
        frame = self.frames[count]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)



class Page1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, background='red')
