import qrcode
import tkinter as tk
from PIL import Image, ImageTk  

# Loop principal da janela
app = tk.Tk()
app.title("Gerador de Qrcode")
app.geometry("1280x720")
app.resizable(False, False)


# qrcode
lbl_qrcode = tk.Label(app, text="")
lbl_qrcode.pack(expand=True)

def PegTexto():
    conteudo = entradaqr.get().strip()

    if not conteudo:
        return

    if conteudo.startswith("www.") or "." in conteudo:
        if not conteudo.startswith(("http://", "https://")):
            conteudo = "https://" + conteudo

    img = qrcode.make(conteudo)
    img = img.resize((400, 400))

    img_tk = ImageTk.PhotoImage(img)
    lbl_qrcode.config(image=img_tk)
    lbl_qrcode.image = img_tk

frame_inferior = tk.Frame(app)
frame_inferior.pack(side="bottom", pady=50)

entradaqr = tk.Entry(frame_inferior, font=("Arial", 20), width=40)
entradaqr.pack(side="left", padx=10)

botao = tk.Button(frame_inferior, text="Gerar QR Code", command=PegTexto, font=("Arial", 15))
botao.pack(side="left")

app.mainloop()