# EVERYTHING ENVOLVING THE POPUP (LABEL, TEXT)

from tkinter import *
from tkinter import font
from PIL import Image,ImageTk

def label(window,imagem):
    popup=PhotoImage(file=imagem)
    label=Label(window,image=popup,bg='#f4bcbc')
    label.image=popup # p/ manter referência (modulização) e não perder a imagem
    label.pack(expand=True)
    return label # o único jeito de manipular a label no main é fazendo com que a função retorne ela

'''O PhotoImage padrão do Tkinter não permite redimensionamento diretamente, 
então usamos PIL (que é como se fosse uma extensão do Tkinter).
Image para abrir, redimensionar e depois converter a imagem.'''

def texto(window):
    global Texto
    fonte_personalizada=font.Font(family='RetroPix Regular',size=24,weight='bold')

    Texto=Label(window,text='clique em qualquer lugar\npara começar',font=fonte_personalizada, 
            bg='#87cbd0',fg='white',justify='center')
    Texto.place(relx=0.3,rely=0.45)
    return Texto

def piscar(window):
    try:
        cor_atual = Texto.cget("fg")
        if cor_atual == 'white':
            nova_cor = '#87cbd0'
        else:
            nova_cor = 'white'
        Texto.config(fg=nova_cor) #aplicando as novas cores ('transparente' e branco)
        window.after(1000, lambda: piscar(window))
    except TclError:
        return
