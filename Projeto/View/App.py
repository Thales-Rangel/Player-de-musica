from GUIs import *


def centralizar_janela(janela):
    janela.update_idletasks()

    largura = janela.winfo_width()
    altura = janela.winfo_height()

    x = (janela.winfo_screenwidth() - largura) // 2
    y = (janela.winfo_screenheight() - altura) // 2 - 30

    janela.geometry(f"{largura}x{altura}+{x}+{y}")
    janela.deiconify()


app = App()
app.title("Player de Música")
app.geometry("1200x720")

centralizar_janela(app)

app.mainloop()
