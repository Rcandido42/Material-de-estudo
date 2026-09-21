import tkinter

#Definindo as variaveis da janela
janela = tkinter.Tk()
janela.title("Simulador de semáforo")
janela.geometry("400x600")

#tkinter.Canvas(...) cria a área de desenho
#janela diz onde o canvas vai ficar
#width=300 define a largura
#height=500 define a altura
canvas = tkinter.Canvas(janela, width=300, height=500)


janela.mainloop()
