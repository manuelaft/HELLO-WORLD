from tkinter import *
from popup import *
from janela import *
from action import *

window = Tk() # instanciando o objeto janela (criando)

fundo=criar_fundo_com_grades(window)

customização(window)

icon(window,'black-crescent-moon.png')

popup_label=label(window,imagem='popup.png') # armazenar em uma variável p/ conseguir remover dps

texto_retorno=texto(window)

piscar(window)

bind(window,popup_label,texto_retorno,fundo)

window.mainloop() # display window
