# EVERYTHING ENVOLVING WNDOW AND ITS CUSTOMIZATION

from tkinter import *
from PIL import Image, ImageTk

def criar_fundo_com_grades(window):
    imagem = Image.open("Imagem_fundo.png")  # sua imagem com grades
    imagem_redimensionada = imagem.resize((800, 600))
    imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)

    fundo = Label(window, image=imagem_tk)
    fundo.image = imagem_tk
    fundo.place(x=0, y=0, relwidth=1, relheight=1)
    fundo.lower()  # garante que fique atrás de tudo
    return fundo

def customização(window):
    window.geometry('800x600') # set size of window
    window.title('PYTHON GUI') # change window title

    '''Everything u need to change in window, use config function. 
    In this case, the background color with their hexadecimal values'''
    window.config(background='#f4c5c5')

def icon(window,image):

    icon=PhotoImage(file=image)
    window.iconphoto(True, icon) # Set the icon to true, then pass the PhotoImage

    '''To change the icon, first it's needed to transform it to a 'PhotoImage', 
    only type of image Tkinter accept'''

def rainbow(window):
    # Abre e redimensiona a imagem
    rainbow_pil = Image.open("rainbow.png")
    rainbow2_pil=Image.open('rainbow2.png')
    rainbowUP_redimensionada = rainbow_pil.resize((240,240))  # define o novo tamanho (largura, altura)
    rainbowDOWN_redimensionada=rainbow2_pil.resize((240,240))
    rainbowUP_tk = ImageTk.PhotoImage(rainbowUP_redimensionada)
    rainbowDOWN_tk=ImageTk.PhotoImage(rainbowDOWN_redimensionada)

    # Cria o Label com a imagem redimensionada
    label_rainbowUP = Label(window, image=rainbowUP_tk, bg="#f4bcbc")
    label_rainbowDOWN=Label(window,image=rainbowDOWN_tk,bg='#f4bcbc')
    label_rainbowUP.image = rainbowUP_tk  # mantém referência
    label_rainbowDOWN.image=rainbowDOWN_tk
    label_rainbowUP.place(relx=0, rely=0)
    label_rainbowDOWN.place(relx=1.0, rely=1.0, anchor='se')  # canto inferior direito)
    label_rainbowUP.lower()
    label_rainbowDOWN.lower()

def animar_letra(widget, relx, rely, passos=10, distancia=0.1, delay=30):
    """Anima o widget com efeito de pulo"""
    # Começa abaixo da posição final
    pos_inicial = rely + distancia
    passo_atual = 0

    def pular():
        nonlocal passo_atual
        y = pos_inicial - (distancia / passos) * passo_atual
        widget.place(relx=relx, rely=y, anchor="center")
        passo_atual += 1
        if passo_atual <= passos:
            widget.after(delay, pular)

    pular()

def letras(window):
    # FUNÇÃO PARA CRIAR IMAGEM COM PULO
    def criar_letra(caminho, relx, rely):
        img_pil = Image.open(caminho).resize((80, 80), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_pil)
        label = Label(window, image=img_tk, bg="#f4bcbc")
        label.image = img_tk  # manter referência
        animar_letra(label, relx, rely)
        return label

    # Cria e anima letra H
    criar_letra("Letra H.png", relx=0.3, rely=0.45)
    criar_letra("Letra E.jpg", relx=0.4, rely=0.45)
    criar_letra('Letra L amarela.png',relx=0.5,rely=0.45)
    criar_letra('Letra L verde.png',relx=0.6,rely=0.45)
    criar_letra('Letra O.png',relx=0.71,rely=0.45)
    criar_letra('Letra W.png',relx=0.3,rely=0.65)
    criar_letra('Letra O verde.png',relx=0.4,rely=0.65)
    criar_letra('Letra R.png',relx=0.5,rely=0.65)
    criar_letra('Letra L laranja.png',relx=0.6,rely=0.65)
    criar_letra('Letra D.png',relx=0.7,rely=0.65)



    # print(popup_original.size) só para descubrir o tamanho da imagem
    original=Image.open('exclamation dot.png')
    original_tk=ImageTk.PhotoImage(original)
    labelex=Label(window,image=original_tk,bg='#f4bcbc')
    labelex.image=original_tk
    labelex.place(relx=0.75,rely=0.58)
