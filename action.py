# EVERYTHING ENVOLVING ACTION

from janela import rainbow,letras

def iniciar(popup_label,texto_retorno,fundo, window):
    print('Nova tela iniciada')
    popup_label.destroy()
    texto_retorno.destroy()
    fundo.destroy()
    letras(window)
    window.after(1000, lambda: rainbow(window))
   
def bind(window,popup_label,texto_retorno,fundo):
    window.bind("<Button-1>", lambda event: iniciar(popup_label,texto_retorno,fundo,window))  # Clique
    window.bind("<Key>", lambda event: iniciar(popup_label,texto_retorno,fundo,window))       # Tecla

    '''Obs: iniciar está sem parentêses porque eu só quero essa função ocorra quando 
    acontecer qualquer um dos eventos, se eu colocar paretênses, é como "chamar" ela,
    logo, vai acontecer independente.'''
